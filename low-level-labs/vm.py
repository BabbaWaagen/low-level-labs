import struct

memory = [0]*256
stack = []
pc = 0

program = [
    ("PUSH",5),
    ("PUSH",3),
    ("ADD",),
    ("PRINT",),
    ("HALT",)
]

running = True

while running:

    instr = program[pc]
    pc += 1

    op = instr[0]

    if op == "PUSH":
        stack.append(instr[1])

    elif op == "ADD":
        b = stack.pop()
        a = stack.pop()
        stack.append(a+b)

    elif op == "SUB":
        b = stack.pop()
        a = stack.pop()
        stack.append(a-b)

    elif op == "PRINT":
        print(stack[-1])

    elif op == "HALT":
        running = False
