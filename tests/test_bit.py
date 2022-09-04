from bit_converter import bit,constant

def test_bit():
    value = 8
    b = bit.Bit(value)
    assert b.to_byte() == value / constant.BYTE
    assert b.to_kilo_bits() == value / constant.KILO_BITS
    assert b.to_mega_bits() == value / constant.MEGA_BITS
    assert b.to_giga_bits() == value / constant.GIGA_BITS
    assert b.to_tera_bits() == value / constant.TERA_BITS