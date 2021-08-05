from enum import Enum


class SimpleEnum(Enum):
    """
    iterの恩恵のためだけにEnumを使っているが他に良い実装がありそう...

    以下を想定
    VALUE = (id, display_name)
    ex) kids = (131, "子供用")

    """

    def get_display_name(self):
        return str(self.value[1])

    def __str__(self):
        return str(self.value[0])

    def __repr__(self):
        return str(self.value[0])

    def __eq__(self, other):
        return str(self) == str(other)
