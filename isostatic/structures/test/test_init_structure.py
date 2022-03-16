
from isostatic import Point, GeneralLoadLineal, Support, Beam, Structure

Structure1 = Structure()

A = Point('A', 0, 0, structure= Structure1)
B = Point('B', 5, 0, structure= Structure1)
C = Point('C', 10, 0, structure= Structure1)

AB = Beam(A, B)
BC = Beam(B, C)

Ra = Support(A, vertical= True, horizontal= True)
Rc = Support(C, vertical=True)

q1 = GeneralLoadLineal(AB, 10,10,0,5,0)
q2 = GeneralLoadLineal(BC, 5, 5, 0, 5, 0)

def test_lists():
    assert Structure1.elements == [AB, BC]
    assert Structure1.points == [A, B, C]
    assert Structure1.supports == [Ra, Rc]
    assert Structure1.loads == [q1, q2] 

