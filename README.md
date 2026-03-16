# computer-science-onefile

Small collection of **single-file computer science projects**.
Most of them are written just for learning and experimenting with **low level programming concepts**, graphics, networking and some system internals.

The idea of this repo is simple:
Every project is **only one file** but still shows some interesting computer science idea.

I made these mostly to understand how things work under the hood, not to build production software. So the code is sometimes a bit messy or simple but it works.

---

# Projects in this Repository

## 1. CPU Emulator

File: `cpu_emulator.py`

This is a **very simple 8-bit CPU emulator** written in Python.
It simulates a tiny processor with registers and instructions.

It supports instructions like:

```
MOV
ADD
SUB
PRINT
HLT
```

Example program:

```
MOV A,5
ADD A,10
SUB A,3
PRINT
HLT
```

Concepts used:

* registers
* instruction decoding
* program counter
* simple ALU logic

This is basically the idea behind how real CPUs execute instructions, just much smaller and simplified.

---

## 2. Cache Simulator

File: `cache_simulator.py`

This script simulates a **very small CPU cache**.

It shows how memory addresses get mapped into a cache and when a **cache hit or miss** happens.

Example output:

```
1 MISS
2 MISS
3 MISS
1 HIT
2 HIT
```

Concepts used:

* memory addressing
* direct mapped cache
* hit/miss statistics

This is something you normally learn in **computer architecture classes**.

---

## 3. Tiny Assembler

File: `tiny_assembler.py`

This is a small **assembler example** that converts a simple assembly language into machine code.

Example:

```
MOV A,5
ADD A,2
SUB A,1
HLT
```

gets converted into binary like:

```
0001000101
0010000010
0011000001
11110000
```

Concepts used:

* instruction sets
* opcodes
* binary encoding
* assembly translation

Real assemblers are much more complex but the idea is similar.

---

## 4. CHIP-8 Emulator

File: `chip8.py`

CHIP-8 is an old **virtual machine from the 1970s**.
Many people build a CHIP-8 emulator as a learning project.

This version implements:

* memory
* registers
* instruction decoding
* simple graphics output

Concepts used:

* emulation
* virtual CPUs
* instruction sets

This is actually the same basic idea used in **game console emulators**.

---

## 5. Minimal Raytracer

File: `raytracer.py`

This is a very small **ray tracer** that renders a sphere using pure Python math.

The renderer shoots rays from a camera and checks if they hit a sphere.

Concepts used:

* vector math
* ray intersection
* lighting calculation
* computer graphics

Output example: a rendered sphere saved as `render.png`.

---

## 6. Software 3D Renderer

File: `renderer3d.py`

This script renders a **rotating 3D cube** using only CPU calculations.

There is no OpenGL or GPU rendering. Everything is done manually.

Concepts used:

* 3D rotation
* perspective projection
* wireframe rendering
* simple graphics pipeline

This shows roughly how early 3D engines worked.

---

## 7. Bitcoin Mining Example

File: `miner.py`

This script demonstrates the basic idea behind **Proof-of-Work mining**.

It repeatedly hashes data using SHA-256 until a hash with enough leading zeros is found.

Example output:

```
Found!
Nonce: 352194
Hash: 0000af32...
```

Concepts used:

* cryptographic hashing
* proof of work
* brute force search

This is basically how Bitcoin mining works, just massively simplified.

---

## 8. TCP Chat Server

File: `chat_server.py`

A small **TCP chat server** using Python sockets.

Multiple clients can connect and messages get broadcast to everyone.

Concepts used:

* TCP networking
* sockets
* multithreading
* client-server architecture

You can connect using netcat or telnet.

Example:

```
telnet localhost 5555
```

---

## 9. Conway's Game of Life

File: `life.py`

Implementation of **Conway’s Game of Life**.

This is a cellular automaton where simple rules produce interesting patterns.

Concepts used:

* simulation
* grid based systems
* emergent behavior
* algorithmic rules

This is a classic example used in computer science.

---

## 10. ELF Binary Inspector

File: `elf_reader.py`

This script reads the header of a **Linux ELF binary**.

Example usage:

```
python elf_reader.py /bin/ls
```

Example output:

```
64-bit ELF
Entry point: 0x401000
```

Concepts used:

* binary file formats
* executable structure
* low level system programming

ELF is the standard executable format on Linux.

---

# Why this repo exists

Most tutorials show how to use libraries but not how things actually work internally.

I wanted to try building some small things that show concepts like:

* how CPUs work
* how graphics rendering works
* how networking works
* how binary formats work
* how cryptography hashing works

These are obviously **very simplified versions**, but they helped me understand the basics better.

---

# Requirements

Some scripts require additional libraries:

```
pygame
numpy
pillow
opencv-python
```

Install them with:

```
pip install pygame numpy pillow opencv-python
```

Other scripts only need the Python standard library.

---

# Running the Programs

Example:

```
python cpu_emulator.py
python raytracer.py
python renderer3d.py
```

Each file runs independently.

---

# Disclaimer

These projects are mostly written for **learning and experimenting**, not optimized or production ready.

Some code might look a bit weird or simple because the goal was just to understand the concepts.

---

# License

MIT License

You can use, modify, and share this code freely.
