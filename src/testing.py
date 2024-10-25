from typenpy.Int import u2, u4, u8, u16, u32, u64, u128, u512, i64
from typenpy.Vector import Vector
from typenpy.Stats import Stats

lista2 = Vector([2, 4 ,6, 6, 53], dtype=u64)

listo = [3, 5, 4, 6]

print(Stats.mode(lista2))