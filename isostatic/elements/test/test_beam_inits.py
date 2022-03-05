from isostatic import Beam
from isostatic import Point

def test_point_addBeam():
    A = Point('A', 0, 0)
    B = Point('B', 4, 0)
    C = Point('C', 10, 0)
    AB = Beam(A, B)
    BC = Beam(B, C)
    assert A.elements == [AB]
    assert B.elements == [AB, BC]
    assert C.elements == [BC]