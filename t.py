from utility import *

memory = bytearray(10*[0x00])

memory[3:5] = hex_slice(0xFFFF)

print(memory)