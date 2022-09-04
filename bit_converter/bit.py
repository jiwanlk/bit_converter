from bit_converter.constant import *


class Bit:
    def __init__(self, bit: int) -> None:
        self.bit = bit

    def to_byte(self):
        return self.bit / BYTE

    def to_kilo_bits(self):
        return self.bit / KILO_BITS

    def to_mega_bits(self):
        return self.bit / MEGA_BITS

    def to_giga_bits(self):
        return self.bit / GIGA_BITS

    def to_tera_bits(self):
        return self.bit / TERA_BITS
