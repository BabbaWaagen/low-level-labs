import sys
import struct

with open(sys.argv[1],"rb") as f:

    data = f.read(64)

magic = data[:4]

if magic != b'\x7fELF':
    print("Not an ELF file")
    exit()

bit = data[4]

if bit == 2:
    print("64-bit ELF")
else:
    print("32-bit ELF")

entry = struct.unpack("<Q",data[24:32])[0]

print("Entry point:",hex(entry))
