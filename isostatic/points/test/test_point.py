from isostatic import Point
from pytest import raises

def test_str_point():
    str_A = "Point: [4, 5, 6]"
    A = Point('A', 4, 5, 6)
    assert str(A) == str_A

    str_B = "Point: []"
    B = Point('B')
    assert str(B) == str_B

    str_C = "Point: [2]"
    C = Point('C',2)
    assert str_C == str(C)

    str_D = "Point: [1, 5, 8, 7, 9]"
    D = Point('D',1, 5, 8, 7, 9)
    assert str(D) == str_D



def test_len_point():
    assert len(Point('A',4,8,2,3,-1,4,2))== 7
    assert len(Point('B',1,2,3)) == 3
    assert len(Point('C',100)) == 1
    assert len(Point('D')) == 0


def test_raises():
    with raises(TypeError):
        Point(5,3,1,2)
    with raises(TypeError):
        Point(True,3,1,2)
    with raises(TypeError):
        Point(False,3,1,2)

    A = Point('Z', 4,5)
    with raises(TypeError):
        A.name = A
    
def test_getters():
    A = Point('A', 1, 2, 3)
    assert A.name == 'A'


def test_setters():
    B = Point('Z', 4, 5, 6)
    B.name = 'B'
    assert  B.name == 'B'
