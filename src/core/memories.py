class BitLimits:
    # Constantes para limites sem sinal (unsigned)
    T2_MAX_UNS = 0x2 # 2

    T4_MAX_UNS = 0x4 # 4

    T8_MAX_UNS = 0xFF  # 255

    T16_MAX_UNS = 0xFFFF  # 65535

    T32_MAX_UNS = 0xFFFFFFFF  # 4294967295

    T64_MAX_UNS = 0xFFFFFFFFFFFFFFFF  # 18446744073709551615

    T128_MAX_UNS = (2**128 - 1)

    T256_MAX_UNS = (2**256 - 1)

    T512_MAX_UNS = (2**512 - 1)

    # Constantes para limites com sinal (signed)
    T8_MAX_SIG = 127
    T8_MIN_SIG = -128

    T16_MAX_SIG = 32767
    T16_MIN_SIG = -32768

    T32_MAX_SIG = 2147483647
    T32_MIN_SIG = -2147483648

    T64_MAX_SIG = 9223372036854775807
    T64_MIN_SIG = -9223372036854775808

    T128_MAX_SIG = (2**127 - 1)
    T128_MIN_SIG = -2**127

    T256_MAX_SIG = (2**255 - 1)
    T256_MIN_SIG = -2**255

    T512_MAX_SIG = (2**511 - 1)
    T512_MIN_SIG = -2**511