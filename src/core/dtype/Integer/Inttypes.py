


from core.memories import BitLimits
from core.dtype.vector.vector_for_Int import Vector

# core.erros has the error messages
from core.errors import (
    BiggerOrLowerNumberError,
    NotIntError
)


bitlmt = BitLimits


__all__ = [
           "i8",
           "i16", 
           "i32", 
           "i64", 
           "i128",
           "i512",
           "u2",
           "u4",
           "u8",
           "u16",
           "u32",
           "u64",
           "u128",
           "u512",
           ]



#--------------The Main Integer Class-----------------------#
class Int():
    """
    Int is an integer data type that extends the basic integer functionalities with custom operations.
    
    Attributes:
        value (int): The integer value stored in the Int instance.

    Methods:
        
        - Adds the current Int value with another integer, Int, or a list of integers.
        >>> num = Int(69)
        >>> num + 3
        Int(72)

        - Subtracts another integer or Int from the current Int value.
        >>> num = Int(69)
        >>> num - 3
        Int(66)
        
        - Multiplies the current Int value with another integer or Int.
        >>> num = Int(69)
        >>> num * 3
        Int(207)
        
        - Divides the current Int value by another integer or Int.
        >>> num = Int(69)
        >>> num / 3
        Int(23)
        

        - Transforms the current Int value into a binary representation and returns it as a string wrapped in an Int.

        >>> num = Int(69)
        >>> num.transformInBinary()
        Int(1000101)
        
            
        - Creates a list of integers from 0 to the current Int value (exclusive) and returns it wrapped in an Int.
        >>> num = Int(3)
        >>> num.for_range()
        Int([0, 1, 2])

        
        - Implements the matrix multiplication operator (@). If the other value is an integer, it multiplies directly.
        If it is a list, each element of the list is multiplied by the current Int value.
  
    """
    def __init__(self, value) -> None:  
        self.value = value


    def __add__(self, other):
        if isinstance(other, int):
            return Int(self.value + other)
        elif isinstance(other, Int):
            return Int(self.value + other.value)
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
    """
    Int2Uns is a subclass of Int that represents an unsigned integer 
    with a limit defined by a specific bit length (2 bits in this case).
    
    """
    def __init__(self, value):
        if not (0 <= value <= bitlmt.T2_MAX_UNS):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T2_MAX_UNS


class Int4Uns(Int):
    """
    Int4Uns is a subclass of Int that represents an unsigned integer 
    with a limit defined by a specific bit length (4 bits in this case).
    
    """
    def __init__(self, value):
        if not (0 <= value <= bitlmt.T4_MAX_UNS):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T4_MAX_UNS


class Int8Uns(Int):
    """
    Int8Uns is a subclass of Int that represents an unsigned integer 
    with a limit defined by a specific bit length (8 bits in this case).
    
    """
    def __init__(self, value):
        if not (0 <= value <= bitlmt.T8_MAX_UNS):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T8_MAX_UNS
    

class Int16Uns(Int):
    """
    Int16Uns is a subclass of Int that represents an unsigned integer 
    with a limit defined by a specific bit length (16 bits in this case).
    
    """
    def __init__(self, value):
        if not (0 <= value <= bitlmt.T16_MAX_UNS):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T16_MAX_UNS


class Int32Uns(Int):
    """
    Int32Uns is a subclass of Int that represents an unsigned integer 
    with a limit defined by a specific bit length (32 bits in this case).
    
    """
    def __init__(self, value):
        if not (0 <= value <= bitlmt.T32_MAX_UNS):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T32_MAX_UNS


class Int64Uns(Int):
    """
    Int64Uns is a subclass of Int that represents an unsigned integer 
    with a limit defined by a specific bit length (64 bits in this case).
    
    """
    def __init__(self, value):
        if not (0 <= value <= bitlmt.T64_MAX_UNS):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T64_MAX_UNS


class Int128Uns(Int):
    """
    Int128Uns is a subclass of Int that represents an unsigned integer 
    with a limit defined by a specific bit length (128 bits in this case).
    
    """
    def __init__(self, value):
        if not (0 <= value <= bitlmt.T128_MAX_UNS):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T128_MAX_UNS


class Int512Uns(Int):
    """
    Int512Uns is a subclass of Int that represents an unsigned integer 
    with a limit defined by a specific bit length (512 bits in this case).
    
    """
    def __ini__(self, value):
        if not (0 <= value <= bitlmt.T512_MAX_UNS):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T512_MAX_UNS


# ================ The Signed Integers Class =========================#


class Int8(Int):
    """
    Int8 is a subclass of Int that represents an 8-bit signed integer.
    
    This class ensures that the value falls within the allowable range of
    -128 to 127, which are the limits for signed 8-bit integers.
    
    """
    def __init__(self, value):
        if not (bitlmt.T8_MIN_SIG <= value <= bitlmt.T8_MAX_SIG):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T8_MAX_SIG
    

class Int16(Int):
    """
    Int16 is a subclass of Int that represents a 16-bit signed integer.
    
    This class ensures that the value falls within the allowable range of
    -32768 to 32767, which are the limits for signed 16-bit integers.
    """
    def __init__(self, value):
        if not (bitlmt.T16_MIN_SIG <= value <= bitlmt.T16_MAX_SIG):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T16_MAX_SIG


class Int32(Int):
    """
    Int32 is a subclass of Int that represents a 32-bit signed integer.
    
    This class ensures that the value falls within the allowable range of
    -2147483648 to 2147483647, which are the limits for signed 32-bit integers.
    
    """
    def __init__(self, value):
        if not (bitlmt.T32_MIN_SIG <= value <= bitlmt.T32_MAX_SIG):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T32_MAX_SIG


class Int64(Int):
    """
    Int64 is a subclass of Int that represents a 64-bit signed integer.
    
    This class ensures that the value falls within the allowable range of
    -9223372036854775808 to 9223372036854775807, which are the limits for signed 64-bit integers.

    """
    def __init__(self, value):
        if not (bitlmt.T64_MIN_SIG <= value <= bitlmt.T64_MAX_SIG):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T64_MAX_SIG


class Int128(Int):
    """
    Int128 is a subclass of Int that represents a 128-bit signed integer.
    
    This class ensures that the value falls within the allowable range of
    -170141183460469231731687303715884105728 to 
    170141183460469231731687303715884105727, which are the limits for signed 128-bit integers.

    """
    def __init__(self, value):
        if not (bitlmt.T128_MIN_SIG <= value <= bitlmt.T128_MAX_SIG):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T128_MAX_SIG


class Int512(Int):
    """
    Int512 is a subclass of Int that represents a 512-bit signed integer.
    
    This class ensures that the value falls within the allowable range of
    -2^511 to 2^511 - 1, which are the limits for signed 512-bit integers.

    """
    def __ini__(self, value):
        if not (bitlmt.T512_MIN_SIG <= value <= bitlmt.T512_MAX_SIG):
            raise BiggerOrLowerNumberError
        self.value = value & bitlmt.T512_MAX_SIG


# Signed Types 
i8 = Int8
i16 = Int16
i32 = Int32
i64 = Int64
i128 = Int128
i512 = Int512

# Unsigned Types

u2   = Int2Uns
u4   = Int4Uns
u8   = Int8Uns
u16  = Int16Uns
u32  = Int32Uns
u64  = Int64Uns
u128 = Int128Uns
u512 = Int512Uns