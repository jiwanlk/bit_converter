from bit_converter import terabit, constant

def test_terabit():
    value = 8
    tb = terabit.Tera_Byte(value)
    assert tb.to_bit() == value * constant.TERA_BITS
    assert tb.to_byte() == value * (constant.TERA_BITS / constant.BYTE)
    assert tb.to_kilo_bits() == value * (constant.TERA_BITS / constant.KILO_BITS)
    assert tb.to_mega_bits() == value * (constant.TERA_BITS / constant.MEGA_BITS)
    assert tb.to_giga_bits() == value * (constant.TERA_BITS / constant.GIGA_BITS)