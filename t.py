from collections import namedtuple

Registers = namedtuple('Registers', 'a b c d e h l sp pc f')
r = Registers(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


a, b, c, d, e, h, l, sp, pc, f = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
reg = bytearray([0xca, 0xfe, 0xba, 0xbe, 0xca, 0xfe, 0xba, 0xbe, 0xff, 0x00])
print(reg[f])


nintendo_logo = bytearray([
    0xCE, 0xED, 0x66, 0x66, 0xCC, 0x0D, 0x00, 0x0B, 0x03, 0x73, 0x00, 0x83, 0x00, 0x0C, 0x00, 0x0D,
    0x00, 0x08, 0x11, 0x1F, 0x88, 0x89, 0x00, 0x0E, 0xDC, 0xCC, 0x6E, 0xE6, 0xDD, 0xDD, 0xD9, 0x99,
    0xBB, 0xBB, 0x67, 0x63, 0x6E, 0x0E, 0xEC, 0xCC, 0xDD, 0xDC, 0x99, 0x9F, 0xBB, 0xB9, 0x33, 0x3E])

with open('LawnBoy.gbc', 'rb') as f:
    print(f.read().find(nintendo_logo))

with open('LawnBoy.gbc', 'rb') as f:
    print(f.read()[0x131])

#class bytearrayc(bytearray):

bb = bytearray([0xff, 0x00])
# bb[0] += 0x01
print(bb)
