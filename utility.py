from typing import Tuple


def hex_slice(x: int) -> Tuple[int, int]:
    assert 0x0 <= x <= 0xFFFF, 'hex_slice: max 16 bits!'
    return x // 0x100, x % 0x100


def hex_compose(x0: int, x1: int) -> int:
    return x0 * 0x100 + x1
