from bit_converter.constant import *


class Kilo_Bit:
    def __init__(self, kb: int) -> None:
        self.kb = kb

    def to_bit(self) -> float:
        return self.kb * KILO_BITS

    def to_byte(self) -> float:
        return self.kb * (KILO_BITS / BYTE)

    def to_mega_bits(self) -> float:
        return self.kb / (MEGA_BITS / KILO_BITS)

    def to_giga_bits(self) -> float:
        return self.kb / (GIGA_BITS / KILO_BITS)

    def to_tera_bits(self) -> float:
        return self.kb / (TERA_BITS / KILO_BITS)
