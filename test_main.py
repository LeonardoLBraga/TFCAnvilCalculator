import unittest

from main import CalculateInstructions
from entities import Instruction, Positions

class TestCalculateInstructions(unittest.TestCase):
    def test_calculateInstructions(self):
        instruction1 = Instruction("lighthit", Positions.LAST)
        instruction2 = Instruction("mediumhit", Positions.SECOND_LAST)
        instruction3 = Instruction("draw", Positions.ANY)

        targetValue = 40

        mandatory_instructions = [instruction1, instruction2, instruction3]

        instructions = ["shrink","shrink","shrink","shrink","draw","mediumhit","lighthit"]

        result = CalculateInstructions(mandatory_instructions, targetValue)
        self.assertEqual(result, instructions)

if __name__ == '__main__':
    unittest.main()
