from isostatic import Point

def test_strPoint():
    str_A = 'Point: (1, 2, 3)'
    A = Point (1, 2, 3)
    assert str_A == str(A)