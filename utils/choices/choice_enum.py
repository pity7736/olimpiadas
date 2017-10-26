from enum import Enum


class ChoiceEnum(Enum):

    @classmethod
    def choices(cls):
        return tuple(((choice.name.lower(), choice.value) for choice in cls))
