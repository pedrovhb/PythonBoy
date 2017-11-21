import sys
from cpu import *

memory = bytearray(0xFFFF*[0x00])
cpu = CPU(memory)

cpu.ld_r_n(0x26, 0xca)  # ld h $ca
cpu.ld_r_n(0x2e, 0xfe)  # ld l $fe
cpu.ld_r_n(0x06, 0xba)  # ld b $ba
cpu.ld_hl_r(0x70)       # ld (hl) b
cpu.ld_r_hl(0x7e)       # ld a (hl)

print(hex(cpu.registers[a]))  # 0xba
print(hex(memory[0xcafe]))