from abc import ABCMeta, abstractmethod


class BaseValidator(metaclass=ABCMeta):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def validate(self):
        pass


class IntegerValidator(BaseValidator):
    def validate(self):
        try:
            res = int(self.value)
            return True, ''
        except ValueError:
            return False, 'Not integer values'


class CharValidator(BaseValidator):
    def __init__(self, value):
        super().__init__(value)

    def validate(self):
        if type(self.value) != str:
            return False, 'Not str values'

        return True, ''
