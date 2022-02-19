from isostatic import Point

def test_str_point():
    str_point = "Point: (4, 5, 6)"
    test_point = Point(4, 5, 6)
    assert str(test_point) == str_point

A = Point(4, 5, 6)
print(A)
str_A = 'Point: (4, 5, 6)'
print(str_A)