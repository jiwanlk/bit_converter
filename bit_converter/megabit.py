from bit_converter.constant import *


class Mega_Bit:
    def __init__(self, mb: int) -> None:
        self.mb = mb

    def to_bit(self) -> float:
        return self.mb * MEGA_BITS

    def to_byte(self) -> float:
        return self.mb * (MEGA_BITS / BYTE)

    def to_kilo_bits(self) -> float:
        return self.mb * (MEGA_BITS / KILO_BITS)

    def to_giga_bits(self) -> float:
        return self.mb / (GIGA_BITS / MEGA_BITS)

    def to_tera_bits(self) -> float:
        return self.mb / (TERA_BITS / MEGA_BITS)
