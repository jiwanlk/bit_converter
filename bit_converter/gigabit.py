from bit_converter.constant import *


class Giga_Bit:
    def __init__(self, gb: int) -> None:
        self.gb = gb

    def to_bit(self) -> float:
        return self.gb * GIGA_BITS

    def to_byte(self) -> float:
        return self.gb * (GIGA_BITS / BYTE)

    def to_kilo_bits(self) -> float:
        return self.gb * (GIGA_BITS / KILO_BITS)

    def to_mega_bits(self) -> float:
        return self.gb * (GIGA_BITS / MEGA_BITS)

    def to_tera_bits(self) -> float:
        return self.gb / (TERA_BITS / GIGA_BITS)
