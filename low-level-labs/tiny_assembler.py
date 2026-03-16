# Tiny Assembler Example

instruction_set = {
    "MOV": "0001",
    "ADD": "0010",
    "SUB": "0011",
    "HLT": "1111"
}

registers = {
    "A": "00",
    "B": "01"
}

program = [
    "MOV A,5",
    "ADD A,2",
    "SUB A,1",
    "HLT"
]

def assemble(line):

    parts = line.split()

    opcode = instruction_set[parts[0]]

    if parts[0] == "HLT":
        return opcode + "0000"

    reg, value = parts[1].split(",")
    reg_bits = registers[reg]

    value_bits = format(int(value), "04b")

    return opcode + reg_bits + value_bits


for instr in program:
    machine = assemble(instr)
    print(instr, "->", machine)
