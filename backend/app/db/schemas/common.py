import random
from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def random_choice(cls):
        return random.choice(cls.list())


class Status(ExtendedEnum):
    INACTIVE = 0
    ACTIVE = 1
    DRAFT = 2
    ARCHIVED = 3
