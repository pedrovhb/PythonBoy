from typing import Tuple


def hex_slice(x: int) -> Tuple[int, int]:

    assert x <= 0xFFFF, 'hex_slice: max 16 bits!'
    return x // 0x100, x % 0x100
