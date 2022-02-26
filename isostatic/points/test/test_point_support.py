from isostatic import Point, Support

def test_stateSupport():
    A = Point('A', 1,2)
    Ra = Support(A, horizontal=True, vertical=True)
    assert A.stateSupport == True