import pytest
import momoko
import datetime
import json

from .test_db import TestDB

from ..project.application.models import Draft
from ..project.base.exceptions import ModelException
from tornado.testing import gen_test


def test_draft():
    dr = Draft.init_by_data(
        {
            'name': '[AUTOSAVE]1467276092380', 'update_date': '2016-06-30 11:42:49',
            'create_date': '2016-06-30 11:42:49', 'relref': '0', 'template': 0, 'reltype': '0',
            'id': '56',
        }
    )

    assert dr.id == '56'

    dr.initial_by_values()

    assert len(dr.fields) == 8
    keys_val = dr.list_keys_and_values()
    assert len(keys_val) == 8

    with pytest.raises(ModelException):
        dr = Draft.init_by_data(
            {
                'ssss': 'test'
            }
        )


class TestDraftDB(TestDB):
    table_name = 'test'


    @gen_test
    def test_save(self):
        dr = Draft.init_by_data(
            {
                'name': '[AUTOSAVE]1467276092380', 'update_date': '2016-06-30 11:42:49',
                'create_date': '2016-06-30 11:42:49', 'relref': '0', 'template': 0, 'reltype': '0',
                'id': '56',
            }
        )

        yield dr.save(self.db, self.table_name)
        res = yield self.db.execute('SELECT count(*) from %s' % self.table_name)
        count = res.fetchone()

        assert count == (2,)

    @gen_test
    def test_all(self):
        dr = Draft.init_by_data(
            {
                'name': '[AUTOSAVE]1467276092380', 'update_date': '2016-06-30 11:42:49',
                'create_date': '2016-06-30 11:42:49', 'relref': '0', 'template': 0, 'reltype': '0',
                'id': '56',
            }
        )

        yield dr.save(self.db, self.table_name)

        res = yield Draft.all(self.db, self.table_name)
        assert len(res) == 1


