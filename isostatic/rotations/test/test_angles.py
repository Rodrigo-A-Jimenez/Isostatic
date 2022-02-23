from sympy import Li
from isostatic import LinealLoad, GeneralLoadLineal
from sympy.abc import E, I 

def test_linealLoads_angles():
    Q = LinealLoad(100,100,10)
    Qleft_angle =  (12500/3)/(E*I)
    Qright_angle = Qleft_angle
    assert Q.angleLeft == Qleft_angle
    assert Q.angleLeft == Q.angleRight
    assert Q.angleRight == Qright_angle

    R = LinealLoad(0,25,6)
    Rright_angle = 105.0/(E*I)
    Rleft_angle = 120.0/(E*I)

    assert R.angleLeft == Rleft_angle
    assert R.angleRight == Rright_angle

def test_generalLoads_to_constantLoads():
    Q = LinealLoad(100,100,10)
    R = GeneralLoadLineal(100, 100, 0, 10, 0)

    assert Q.angleLeft == R.angleLeft
    assert Q.angleRight == R.angleRight
    

    A = LinealLoad(0,25,6)
    B = GeneralLoadLineal(0, 25, 0, 6, 0)
    assert A.angleLeft == B.angleLeft
    assert A.angleRight == B.angleRight
