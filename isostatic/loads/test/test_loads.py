from isostatic import LinealLoad, GeneralLoadLineal, Beam
from sympy.abc import E, I

from isostatic.points.point import Point 

testPoint_1 = Point('aux1', 0, 0)
testPoint_2 = Point('aux2', 5, 0)
beam = Beam(testPoint_1, testPoint_2)

def test_linealLoads_angles():
    Q = LinealLoad(100,100,10)
    Qleft_angle =  (12500/3)/(E*I)
    Qright_angle = Qleft_angle
    assert Q.leftAngle == Qleft_angle
    assert Q.leftAngle == Q.rightAngle
    assert Q.rightAngle == Qright_angle

    R = LinealLoad(0,25,6)
    Rright_angle = 105.0/(E*I)
    Rleft_angle = 120.0/(E*I)

    assert R.leftAngle == Rleft_angle
    assert R.rightAngle == Rright_angle


def test_generalLoads_to_constantLoads():
    
    Q = LinealLoad(100,100,10)
    R = GeneralLoadLineal(beam, 100, 100, 0, 10, 0)

    assert Q.leftAngle == R.leftAngle
    assert Q.rightAngle == R.rightAngle
    

    A = LinealLoad(0,25,6)
    B = GeneralLoadLineal(beam, 0, 25, 0, 6, 0)
    assert A.leftAngle == B.leftAngle
    assert A.rightAngle == B.rightAngle

def test_diferent_i_and_e():
    Q = GeneralLoadLineal(beam, 10, 10, 0, 4, 0, E= 2*E)
    wi = 26.6666666666666666667/(2*E*I)

    assert Q.leftAngle == wi

def test_loadTotal():
    Q = GeneralLoadLineal(beam,10,15,2,5,0)
    Rq = (10+15)/2 * 5

    Q1 = GeneralLoadLineal(beam,0,100,10,3,10)
    Rq1 = 100*3/2

    Q2 = GeneralLoadLineal(beam,25,25,0,7,0)
    Rq2 = 25*7

    assert Q.loadTotal() == Rq
    assert Q1.loadTotal() == Rq1
    assert Q2.loadTotal() == Rq2