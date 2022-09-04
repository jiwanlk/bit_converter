from bit_converter.constant import *


class Tera_Byte:
    def __init__(self, tb: int) -> None:
        self.tb = tb

    def to_bit(self) -> float:
        return self.tb * TERA_BITS

    def to_byte(self) -> float:
        return self.tb * (TERA_BITS / BYTE)

    def to_kilo_bits(self) -> float:
        return self.tb * (TERA_BITS / KILO_BITS)

    def to_mega_bits(self) -> float:
        return self.tb * (TERA_BITS / MEGA_BITS)

    def to_giga_bits(self) -> float:
        return self.tb * (TERA_BITS / GIGA_BITS)
