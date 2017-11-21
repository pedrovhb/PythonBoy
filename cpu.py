from utility import hex_slice

# Registers
a, f, b, c, d, e, h, l = 0, 1, 2, 3, 4, 5, 6, 7
sp, pc = slice(8, 9), slice(10, 11)
af, bc, de, hl = slice(a, f), slice(b, c), slice(d, e), slice(h, l)

class CPU:

    def __init__(self):
        self.registers = bytearray(11*[0x00])
        self.init_cpu()

    def init_cpu(self):
        # Set Program Counter to 0x100
        self.registers[pc] = hex_slice(0x0100)

        # Set Stack Pointer to 0xFFFE
        self.registers[sp] = hex_slice(0xFFFE)

    # 8-bit load instructions, all take 8 cycles
    def ld(self, opcode, n):
        register_opcode = {0x06: b, 0x0e: c, 0x16: d, 0x1e: e, 0x26: h, 0x2e: l}
        self.registers[register_opcode[opcode]] = n

    def __str__(self):
        # todo - this is pretty terrible
        s = ''.join(['{}: {}\n'.format(ch, hex(self.registers[i])) for i, ch in enumerate('afbcdehl')])
        # s += 'sp: {}\tpc: {}'.format(hex(self.registers[sp][0]), hex(sum(self.registers[pc])))
        return s




c = CPU()
c.ld(0x06, 0xFE)
c.ld(0x1e, 0x13)
c.ld(0x26, 0x37)
print(c)