from sympy import Symbol
from isostatic import Support, Point

def test_istances():
    A = Point('A', 0, 0)
    RA = Support(A, vertical=True)
    str_RA = 'Support A: [0, 0]'
    test_var = [Symbol('vert_A')]

    assert isinstance(RA, Support)
    assert str(RA) == str_RA
    assert RA.vars == test_var
    '''
    Errores en los tipos proporcionados(RESUELTO)
    '''