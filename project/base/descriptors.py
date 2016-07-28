from .exceptions import ModelException


class BaseDescriptor:
    def __init__(self, column_name=None, validators=[]):
        self._validators = validators
        self._column_name = column_name
        self._value = None

    def __set__(self, instance, value):
        for valid in self._validators:
            validators = valid(value)
            status, message = validators.validate()
            if not status:
                raise ModelException(message)
        self._value = value

    def __get__(self, instance, owner):
        return self._value

    @property
    def column_name(self):
        return self._column_name


class SimpleField(BaseDescriptor):
    pass


class LenField(BaseDescriptor):
    def __init__(self, max_length, column_name=None, validators=[]):
        super().__init__(column_name, validators)
        self._max_length = max_length

    def __set__(self, instance, value):

        self.validate(value)
        super().__set__(instance, value)

    def validate(self, value):
        if len(value) > self._max_length:
            raise ModelException('More len then possible')
