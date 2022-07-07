
from curve_point import Affine_Point
from ellipticCurve import Ell_Curve, n

x, y = Ell_Curve.find_point()
affine_point = Affine_Point(x, y)
projective_point = affine_point.Affine_To_Projective_Point()

O_E = projective_point * n
result = O_E.Projective_To_Affine_Point()

print(result)

