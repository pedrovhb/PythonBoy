f = 0x00

f_z, f_n, f_h, f_c = 0b10000000, 0b01000000, 0b00100000, 0b00010000


def set_flag(flag, value):  # Modify Zero flag
    global f
    f |= flag
    if not value:
        f ^= flag

flag_z(1)
print(bin(f))

flag_z(1)
print(bin(f))

flag_z(0)
print(bin(f))

flag_z(0)
print(bin(f))

flag_z(1)
print(bin(f))
