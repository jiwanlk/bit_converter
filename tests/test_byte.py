from bit_converter import byte, constant

def test_byte():
    value = 8
    B = byte.Byte(value)
    assert B.to_bit() == value * constant.BYTE
    assert B.to_kilo_bits() == value / (constant.KILO_BITS / constant.BYTE)
    assert B.to_mega_bits() == value / (constant.MEGA_BITS / constant.BYTE)
    assert B.to_giga_bits() == value / (constant.GIGA_BITS / constant.BYTE)
    assert B.to_tera_bits() == value / (constant.TERA_BITS / constant.BYTE)