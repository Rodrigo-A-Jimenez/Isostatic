from isostatic import Point

def test_str_point():
    str_A = "Point: [4, 5, 6]"
    A = Point(4, 5, 6)
    assert str(A) == str_A

    str_B = "Point: []"
    B = Point()
    assert str(B) == str_B

    str_C = "Point: [2]"
    C = Point(2)
    assert str_C == str(C)

    str_D = "Point: [1, 5, 8, 7, 9]"
    D = Point(1, 5, 8, 7, 9)
    assert str(D) == str_D


def test_len_point():
    assert len(Point(4,8,2,3,-1,4,2))== 7
    assert len(Point(1,2,3)) == 3
    assert len(Point(100)) == 1
    assert len(Point()) == 0