from ..base.base_model import Model
from ..base.validators import IntegerValidator, CharValidator
from ..base.descriptors import SimpleField, LenField


class Draft(Model):
    id = SimpleField(column_name='id_sendsay', validators=[IntegerValidator])
    alias = LenField(max_length=250, validators=[CharValidator])
    name = LenField(max_length=250, validators=[CharValidator])
    template = SimpleField(validators=[IntegerValidator])
    create_date = SimpleField(validators=[])
    update_date = SimpleField(validators=[])
    reltype = SimpleField(validators=[])
    relref = SimpleField(validators=[])

