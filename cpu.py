from utility import hex_slice, hex_compose

# Registers
a, f, b, c, d, e, h, l = 0, 1, 2, 3, 4, 5, 6, 7
sp, pc = slice(8, 9+1), slice(10, 11+1)
af, bc, de, hl = slice(a, f+1), slice(b, c+1), slice(d, e+1), slice(h, l+1)


class CPU:
    def __init__(self, memory):
        self.memory = memory
        self.registers = bytearray(11 * [0x00])
        self.init_cpu()

    def init_cpu(self):
        # Set Program Counter to 0x100
        self.registers[pc] = hex_slice(0x0100)

        # Set Stack Pointer to 0xFFFE
        self.registers[sp] = hex_slice(0xFFFE)

    # 8-bit load instructions, n to reg
    def ld_r_n(self, opcode, n):  # 8 cycles
        register_opcode = {0x06: b, 0x0e: c, 0x16: d, 0x1e: e, 0x26: h, 0x2e: l}
        self.registers[register_opcode[opcode]] = n

    # 8-bit load instructions, reg to reg
    def ld_r1_r2(self, opcode):  # 4 cycles
        register_opcode = {0x7f: (a, a), 0x78: (a, b), 0x79: (a, c), 0x7a: (a, d), 0x7b: (a, e), 0x7c: (a, h),
                           0x7d: (a, l), 0x40: (b, b), 0x41: (b, c), 0x42: (b, d), 0x43: (b, e), 0x44: (b, h),
                           0x45: (b, l), 0x48: (c, b), 0x49: (c, c), 0x4a: (c, d), 0x4b: (c, e), 0x4c: (c, h),
                           0x4d: (c, l), 0x50: (d, b), 0x51: (d, c), 0x52: (d, d), 0x53: (d, e), 0x54: (d, h),
                           0x55: (d, l), 0x58: (e, b), 0x59: (e, c), 0x5a: (e, d), 0x5b: (e, e), 0x5c: (e, h),
                           0x5d: (e, l), 0x60: (h, b), 0x61: (h, c), 0x62: (h, d), 0x63: (h, e), 0x64: (h, h),
                           0x65: (h, l), 0x68: (l, b), 0x69: (l, c), 0x6a: (l, d), 0x6b: (l, e), 0x6c: (l, h),
                           0x6d: (l, l)}

        self.registers[register_opcode[opcode][0]] = self.registers[register_opcode[opcode][1]]

    # 8-bit load instructions, reg to (hl)
    def ld_hl_r(self, opcode):  # 8 cycles
        hl_loc = hex_compose(*self.registers[hl])
        register_opcode = {0x70: b, 0x71: c, 0x72: d, 0x73: e, 0x74: h, 0x75: l}
        self.memory[hl_loc] = self.registers[register_opcode[opcode]]

    # 8-bit load instructions, (hl) to reg
    def ld_r_hl(self, opcode):  # 8 cycles
        h1_loc = hex_compose(*self.registers[hl])
        register_opcode = {0x66: h, 0x5e: e, 0x56: d, 0x4e: c, 0x46: b, 0x7e: a, 0x6e: l}
        self.registers[register_opcode[opcode]] = self.memory[h1_loc]

    # todo: implement instruction 0x36: ld (hl),n (12 cycles)

    def __str__(self):
        # todo - this is pretty terrible
        s = ''.join(['{}: {}\n'.format(ch, hex(self.registers[i])) for i, ch in enumerate('afbcdehl')])
        # s += 'sp: {}\tpc: {}'.format(hex(self.registers[sp][0]), hex(sum(self.registers[pc])))
        return s
