import pygame
import sys
import random

MEMORY_SIZE = 4096
WIDTH = 64
HEIGHT = 32

class Chip8:
    def __init__(self):
        self.memory = [0] * MEMORY_SIZE
        self.V = [0] * 16
        self.I = 0
        self.pc = 0x200
        self.stack = []
        self.display = [[0]*WIDTH for _ in range(HEIGHT)]

    def load_program(self, filename):
        with open(filename, "rb") as f:
            program = f.read()

        for i, b in enumerate(program):
            self.memory[0x200+i] = b

    def cycle(self):
        opcode = self.memory[self.pc] << 8 | self.memory[self.pc+1]
        self.pc += 2

        if opcode == 0x00E0:  # clear screen
            self.display = [[0]*WIDTH for _ in range(HEIGHT)]

        elif opcode == 0x00EE:  # return
            self.pc = self.stack.pop()

        elif opcode & 0xF000 == 0x1000:  # jump
            self.pc = opcode & 0x0FFF

        elif opcode & 0xF000 == 0x6000:  # set register
            x = (opcode & 0x0F00) >> 8
            self.V[x] = opcode & 0x00FF

        elif opcode & 0xF000 == 0x7000:  # add
            x = (opcode & 0x0F00) >> 8
            self.V[x] += opcode & 0x00FF


def draw_display(screen, chip):
    screen.fill((0,0,0))
    scale = 10

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if chip.display[y][x]:
                pygame.draw.rect(screen,(255,255,255),
                                 (x*scale,y*scale,scale,scale))

    pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((640,320))
    clock = pygame.time.Clock()

    chip = Chip8()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        chip.cycle()
        draw_display(screen, chip)

        clock.tick(500)


if __name__ == "__main__":
    main()
