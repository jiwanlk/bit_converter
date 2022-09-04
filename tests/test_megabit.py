from bit_converter import megabit, constant

def test_megabit():
    value = 8
    mb = megabit.Mega_Bit(value)
    assert mb.to_bit() == value * constant.MEGA_BITS
    assert mb.to_byte() == value * (constant.MEGA_BITS / constant.BYTE)
    assert mb.to_kilo_bits() == value * (constant.MEGA_BITS / constant.KILO_BITS)
    assert mb.to_giga_bits() == value / (constant.GIGA_BITS / constant.MEGA_BITS)
    assert mb.to_tera_bits() == value / (constant.TERA_BITS / constant.MEGA_BITS)