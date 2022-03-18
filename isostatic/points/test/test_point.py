from isostatic import Point, Structure
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

def test_modulus():
    A = Point('A', 3, 4)
    modA = 5
    assert A.modulus() == modA

    B = Point('B',2,2,-1)
    modB = 3
    assert B.modulus() == modB

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

def test_operations():
    e1 = Point('e1', 5, -2)
    e2 = Point('e2', 5, -2)
    assert e1 == e2

    A = Point('A',5,3)
    B = Point('B',0,5)
    AB = A + B
    A_B = Point('AB', 5, 8)
    assert AB == A_B

    C = Point('C', 1, -2)
    D = Point('D', 5, 2)
    CD = Point('C-D', -4, -4)
    assert (C-D) == CD
    
    E = Point('E', 2, -2)
    n = 2.0
    m = 5
    E_div1 = Point('E/', 1, -1)
    E_div2 = Point('E/', 2/5, -2/5)
    
    assert (E/n) == E_div1
    assert (E/m) == E_div2