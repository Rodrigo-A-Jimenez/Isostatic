from pytest import raises

from isostatic import Point, Support, Structure

frame = Structure()

def test_stateSupport():
    A = Point('A', 1, 2)
    Ra = Support(A, horizontal=True, vertical=True)
    assert A.stateSupport == True

def test_raises():
    A = Point('A', 1, 2)
    Ra = Support(A, horizontal=True, vertical=True)
    with raises(ValueError):
        R_a = Support(A, horizontal=True, moment=True)

