from bit_converter import gigabit, constant

def test_gigabit():
    value = 8
    gb = gigabit.Giga_Bit(value)
    assert gb.to_bit() == value * constant.GIGA_BITS
    assert gb.to_byte() == value * (constant.GIGA_BITS / constant.BYTE)
    assert gb.to_kilo_bits() == value * (constant.GIGA_BITS / constant.KILO_BITS)
    assert gb.to_mega_bits() == value * (constant.GIGA_BITS / constant.MEGA_BITS)
    assert gb.to_tera_bits() == value / (constant.TERA_BITS / constant.GIGA_BITS)