from bit_converter.constant import *


class Byte:
    def __init__(self, byte: int) -> None:
        self.byte = byte

    def to_bit(self) -> float:
        return self.byte * BYTE

    def to_kilo_bits(self) -> float:
        return self.byte / (KILO_BITS / BYTE)

    def to_mega_bits(self) -> float:
        return self.byte / (MEGA_BITS / BYTE)

    def to_giga_bits(self) -> float:
        return self.byte / (GIGA_BITS / BYTE)

    def to_tera_bits(self) -> float:
        return self.byte / (TERA_BITS / BYTE)
