from core.memories import BitLimits

from core.errors import (
    BiggerOrLowerNumberError,
    NotIntError
)

bitlmt = BitLimits


#--------------The Main Integer Class-----------------------#
class Int():
    def __init__(self, value) -> None:  
        self.value = value


    def __add__(self, other):
        if isinstance(other, int):
            return Int(self.value + other)
        elif isinstance(other, Int):
            return Int(self.value + other.value)
        elif isinstance(other, list):
            list_ = []
            for elem in other:
                list_.append(elem + self.value)
            return Int(list_) # Might create a list dtype for that
        else:
            raise NotIntError
        
    def __sub__(self, other):
        if isinstance(other, int):
            return Int(self.value - other)
        elif isinstance(other, Int):
            return Int(self.value - other.value)
        else:
            raise NotIntError
        
    def __mul__(self, other):
        if isinstance(other, int):
            return Int(self.value * other)
        elif isinstance(other, Int):
            return Int(self.value * other.value)
        else:
            raise NotIntError
        
    def __truediv__(self, other):
        if isinstance(other, int):
            return Int(self.value / other)
        elif isinstance(other, Int):
            return Int(self.value / other.value)
        else:
            raise NotIntError
        
    def transformInBinary(self):
        binary = bin(self.value)[2:]

        return Int(binary)
    
    def for_range(self):
        list = []

        for i in range(self.value):
            list.append(i)
        return Int(list)
    
    def __matmul__(self, other):
        list = []

        if isinstance(other, int):
            return Int(self.value * other)
        elif isinstance(other, list):
            for elem in other:
                list.append(elem * self.value)
        return Int(list)
        
    
    def __repr__(self) -> str:
        return f"Int({self.value})"


# ================ The Unsigned Integers Class =========================#

class Int2Uns(Int):
    def __init__(self, value):
        if not (0 <= value <= bitlmt.T2_MAX_UNS):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T2_MAX_UNS


class Int4Uns(Int):
    def __init__(self, value):
        if not (0 <= value <= bitlmt.T4_MAX_UNS):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T4_MAX_UNS


class Int8Uns(Int):
    def __init__(self, value):
        if not (0 <= value <= bitlmt.T8_MAX_UNS):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T8_MAX_UNS
    

class Int16Uns(Int):
    def __init__(self, value):
        if not (0 <= value <= bitlmt.T16_MAX_UNS):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T16_MAX_UNS


class Int32Uns(Int):
    def __init__(self, value):
        if not (0 <= value <= bitlmt.T32_MAX_UNS):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T32_MAX_UNS


class Int64Uns(Int):
    def __init__(self, value):
        if not (0 <= value <= bitlmt.T64_MAX_UNS):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T64_MAX_UNS


class Int128Uns(Int):
    def __init__(self, value):
        if not (0 <= value <= bitlmt.T128_MAX_UNS):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T128_MAX_UNS


class Int512Uns(Int):
    def __ini__(self, value):
        if not (0 <= value <= bitlmt.T512_MAX_UNS):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T512_MAX_UNS


u2 = Int2Uns
u4 = Int4Uns
u8 = Int8Uns
u16 = Int16Uns
u32 = Int32Uns
u64 = Int64Uns
u128 = Int128Uns
u512 = Int512Uns