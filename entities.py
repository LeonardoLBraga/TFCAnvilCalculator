from enum import Enum

class Positions(Enum):
    NONE = "None"
    NOT_LAST = "NotLast"
    LAST = "Last"
    SECOND_LAST = "SecondLast"
    THIRD_LAST = "ThirdLast"
    ANY = "Any"

class Instruction:
    def __init__(self, name: str, position: Positions):
        self.name = name
        self.position = position
        self.value = self.complete_value_by_name()

    def complete_value_by_name(self):
        values_by_name = {
            "lighthit": -3,
            "mediumhit": -6,
            "hardhit": -9,
            "draw": -15,
            "punch": 2,
            "bend": 7,
            "upset": 13,
            "shrink": 16
        }
        return values_by_name.get(self.name, 0)