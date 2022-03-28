from sympy import vectorize
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
    
def test_vector_force_moment():
    v = Vector(2, 10)
    assert v.forceMoment() == -20
    
    v1 = Vector(2, [-4, -3])
    assert v1.forceMoment() == -6

def test_vector_add():
    v1 = Vector(2, [-4, -3])
    v2 = Vector(6, [1, 2])
    v3 = v1 + v2
    assert v3.notation == [-3, -1]
    
    u1 = Vector(5, 10)
    u2 = Vector(4, 11)
    u3 = u1 + u2
    assert u3.notation == [0, -21]