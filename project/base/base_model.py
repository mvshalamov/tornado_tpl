import inspect

from .exceptions import ModelException
from .descriptors import BaseDescriptor


class ModelMeta(type):
    def __new__(mcs, name, bases, dct):
        fields = {
            attr_name: {
                "name_table_column": val.column_name, "value": None
            } for (attr_name, val) in dct.items() if isinstance(val, BaseDescriptor)
        }

        dct['fields'] = fields
        return type.__new__(mcs, name, bases, dct)


class Model(metaclass=ModelMeta):
    @classmethod
    def init_by_data(cls, init_data):
        attrs = [attr for attr in dir(cls) if not inspect.ismethod(attr)]
        obj = cls()

        for key, value in init_data.items():
            key = key.replace('.', '_')
            if key not in attrs:
                raise ModelException('Attribute - %s, not find in model' % key)
            setattr(obj, key, value)
        obj.initial_by_values()
        return obj

    def initial_by_values(self):
        """
        вызываем при изменение атрибутов модели
        :return: None
        """
        for key in self.fields:
            self.fields[key]['value'] = getattr(self, key)

    def list_keys_and_values(self):
        """
        :return:
        """
        return [(v['name_table_column'] if v['name_table_column'] else k, v['value']) for k, v in self.fields.items()]

    async def save(self, db, table_name):
        self.initial_by_values()
        values = self.list_keys_and_values()

        sql_data = """
            INSERT INTO {table_name} (
              {columns_names}
            ) VALUES (
              {variables}
            );
        """.format(
            variables=','.join('%s' for v in values), table_name=table_name, columns_names=','.join(v[0] for v in values)
        )

        conn = await db.getconn()
        with db.manage(conn):
            sql_data = conn.mogrify(
                sql_data, [v[1] for v in values]
            )

            res = await conn.execute(
                sql_data
            )

            return res

    @classmethod
    async def all(cls, db, table_name):
        sql_data = """
            select * from {table_name};
        """.format(
                table_name=table_name,
        )
        conn = await db.getconn()
        with db.manage(conn):
            sql_data = conn.mogrify(sql_data)

            res = await conn.execute(
                sql_data
            )
            return res.fetchall()
