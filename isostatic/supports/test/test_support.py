from isostatic import Support, Point

def test_istances():
    A = Point('A', 0, 0)
    RA = Support(A, vertical=True)
    assert isinstance(RA, Support)

    '''
    Errores en los tipos proporcionados
    '''