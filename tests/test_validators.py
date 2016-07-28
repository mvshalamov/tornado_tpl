import pytest

from ..project.base.validators import IntegerValidator, CharValidator, BaseValidator


def test_integervalidator():
    intval1 = IntegerValidator(10)
    assert (True, '') == intval1.validate()
    intval2 = IntegerValidator('sdfsdfs')
    assert (False, 'Not integer values') == intval2.validate()


def test_charvalidator():
    charval1 = CharValidator('sdfsdfs')
    assert (True, '') == charval1.validate()

    charval2 = CharValidator({})
    assert (False, 'Not str values') == charval2.validate()

