from isostatic import Point, Support, ModelEstructure
frame = ModelEstructure()

def test_stateSupport():
    A = Point('A', 1, 2)
    Ra = Support(A, horizontal=True, vertical=True)
    assert A.stateSupport == True