from entities import Instruction, Positions


def AddInstructionsByPosition(instructions, mandatory_instructions):
    first_candidates = [Positions.THIRD_LAST, Positions.ANY, Positions.NOT_LAST]
    second_candidates = [Positions.SECOND_LAST, Positions.ANY, Positions.NOT_LAST]
    third_candidates = [Positions.LAST, Positions.ANY]

    first = next((i for i in mandatory_instructions if i.position in first_candidates), None)
    second = next((i for i in mandatory_instructions if i != first and i.position in second_candidates), None)
    third = next((i for i in mandatory_instructions if i not in [first, second] and i.position in third_candidates), None)

    if first:
        instructions.append(first.name)
    if second:
        instructions.append(second.name)
    if third:
        instructions.append(third.name)


def CalculateInstructions(mandatory_instructions, targetValue):
    instructions = []

    valueWithInstructions = targetValue - mandatory_instructions[0].value - mandatory_instructions[1].value - mandatory_instructions[2].value

    while valueWithInstructions >= 16:
        valueWithInstructions -= 16
        instructions.append("shrink")
    
    value_to_instructions = {
        15: ["upset", "punch"],
        14: ["bend", "bend"],
        13: ["upset"],
        12: ["shrink", "mediumhit", "punch"],
        11: ["upset"],
        10: ["shrink", "mediumhit"],
        9: ["bend", "punch"],
        8: ["punch", "punch", "punch", "punch"],
        7: ["bend"],
        6: ["punch", "punch", "punch"],
        5: ["punch", "punch", "punch", "punch", "lighthit"],
        4: ["punch", "punch"],
        3: ["punch", "bend", "mediumhit"],
        2: ["punch"],
        1: ["shrink", "draw"]
    }

    if valueWithInstructions in value_to_instructions:
        instructions.extend(value_to_instructions[valueWithInstructions])

    AddInstructionsByPosition(instructions, mandatory_instructions)

    return instructions


def main(): 
    instruction1 = Instruction("draw", Positions.NOT_LAST)
    instruction2 = Instruction("hardhit", Positions.NOT_LAST)
    instruction3 = Instruction("shrink", Positions.LAST)

    targetValue = 40

    mandatory_instructions = [instruction1, instruction2, instruction3]

    instructionsFinal = CalculateInstructions(mandatory_instructions, targetValue)
    print("final_instruction: ", instructionsFinal)


if __name__ == "__main__":
    main()