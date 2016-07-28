import pytest

from ..project.base.exceptions import ModelException
from ..project.base.descriptors import SimpleField, LenField
from ..project.base.validators import IntegerValidator


def test_descriptors():
    class T:
        first = SimpleField(column_name='a1', validators=[IntegerValidator])
        second = LenField(max_length=10, validators=[])

    desc = T()
    desc.first = 10
    assert 10 == desc.first

    desc.second = "sd"
    assert desc.second == "sd"
    with pytest.raises(ModelException):
        desc.first = 'sdfsdfsdfsdf'

    with pytest.raises(ModelException):
        desc.second = "jsxzczxczxczxczxcjksdjksdjfksdjfklsdfzxc"

    first = SimpleField(column_name='a1', validators=[])
    assert first.column_name == 'a1'
