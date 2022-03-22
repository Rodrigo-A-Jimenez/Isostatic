from isostatic.points.vectors import Vector
from math import atan

def test_vector_init():
    pass

def test_vector_notation():
    v = Vector(2, 10)
    assert v.notation == [0, -10]
    
    v1 = Vector(2, [-4, -3])
    assert v1.notation == [-4, -3]
    assert v1.module == 5