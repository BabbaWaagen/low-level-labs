# Simple 8-bit CPU Emulator

class CPU:
    def __init__(self):
        self.A = 0
        self.B = 0
        self.pc = 0
        self.running = True

    def execute(self, program):
        while self.running and self.pc < len(program):
            instr = program[self.pc]
            self.pc += 1
            self.run_instruction(instr)

    def run_instruction(self, instr):
        parts = instr.split()

        if parts[0] == "MOV":
            reg, val = parts[1].split(",")
            val = int(val)

            if reg == "A":
                self.A = val
            elif reg == "B":
                self.B = val

        elif parts[0] == "ADD":
            reg, val = parts[1].split(",")
            val = int(val)

            if reg == "A":
                self.A += val

        elif parts[0] == "SUB":
            reg, val = parts[1].split(",")
            val = int(val)

            if reg == "A":
                self.A -= val

        elif parts[0] == "PRINT":
            print("A =", self.A)

        elif parts[0] == "HLT":
            self.running = False


program = [
    "MOV A,5",
    "ADD A,10",
    "SUB A,3",
    "PRINT",
    "HLT"
]

cpu = CPU()
cpu.execute(program)
