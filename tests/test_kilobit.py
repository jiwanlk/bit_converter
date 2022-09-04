from bit_converter import kilobit, constant

def test_kilobit():
    value = 8
    kb = kilobit.Kilo_Bit(value)
    assert kb.to_bit() == value * constant.KILO_BITS
    assert kb.to_byte() == value * (constant.KILO_BITS / constant.BYTE)
    assert kb.to_mega_bits() == value / (constant.MEGA_BITS / constant.KILO_BITS)
    assert kb.to_giga_bits() == value / (constant.GIGA_BITS / constant.KILO_BITS)
    assert kb.to_tera_bits() == value / (constant.TERA_BITS / constant.KILO_BITS)
