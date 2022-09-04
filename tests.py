from bit_converter import bit, byte, constant, kilobit, megabit, gigabit, terabit


def test_bit():
    value = 8
    b = bit.Bit(value)
    assert b.to_byte() == value / constant.BYTE
    assert b.to_kilo_bits() == value / constant.KILO_BITS
    assert b.to_mega_bits() == value / constant.MEGA_BITS
    assert b.to_giga_bits() == value / constant.GIGA_BITS
    assert b.to_tera_bits() == value / constant.TERA_BITS


def test_byte():
    value = 8
    B = byte.Byte(value)
    assert B.to_bit() == value * constant.BYTE
    assert B.to_kilo_bits() == value / (constant.KILO_BITS / constant.BYTE)
    assert B.to_mega_bits() == value / (constant.MEGA_BITS / constant.BYTE)
    assert B.to_giga_bits() == value / (constant.GIGA_BITS / constant.BYTE)
    assert B.to_tera_bits() == value / (constant.TERA_BITS / constant.BYTE)


def test_kilobit():
    value = 8
    kb = kilobit.Kilo_Bit(value)
    assert kb.to_bit() == value * constant.KILO_BITS
    assert kb.to_byte() == value * (constant.KILO_BITS / constant.BYTE)
    assert kb.to_mega_bits() == value / (constant.MEGA_BITS / constant.KILO_BITS)
    assert kb.to_giga_bits() == value / (constant.GIGA_BITS / constant.KILO_BITS)
    assert kb.to_tera_bits() == value / (constant.TERA_BITS / constant.KILO_BITS)


def test_megabit():
    value = 8
    mb = megabit.Mega_Bit(value)
    assert mb.to_bit() == value * constant.MEGA_BITS
    assert mb.to_byte() == value * (constant.MEGA_BITS / constant.BYTE)
    assert mb.to_kilo_bits() == value * (constant.MEGA_BITS / constant.KILO_BITS)
    assert mb.to_giga_bits() == value / (constant.GIGA_BITS / constant.MEGA_BITS)
    assert mb.to_tera_bits() == value / (constant.TERA_BITS / constant.MEGA_BITS)


def test_gigabit():
    value = 8
    gb = gigabit.Giga_Bit(value)
    assert gb.to_bit() == value * constant.GIGA_BITS
    assert gb.to_byte() == value * (constant.GIGA_BITS / constant.BYTE)
    assert gb.to_kilo_bits() == value * (constant.GIGA_BITS / constant.KILO_BITS)
    assert gb.to_mega_bits() == value * (constant.GIGA_BITS / constant.MEGA_BITS)
    assert gb.to_tera_bits() == value / (constant.TERA_BITS / constant.GIGA_BITS)


def test_terabit():
    value = 8
    tb = terabit.Tera_Byte(value)
    assert tb.to_bit() == value * constant.TERA_BITS
    assert tb.to_byte() == value * (constant.TERA_BITS / constant.BYTE)
    assert tb.to_kilo_bits() == value * (constant.TERA_BITS / constant.KILO_BITS)
    assert tb.to_mega_bits() == value * (constant.TERA_BITS / constant.MEGA_BITS)
    assert tb.to_giga_bits() == value * (constant.TERA_BITS / constant.GIGA_BITS)


if __name__ == "__main__":
    test_bit()
    test_byte()
    test_kilobit()
    test_megabit()
    test_gigabit()
    test_terabit()
