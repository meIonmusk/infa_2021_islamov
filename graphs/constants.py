from scipy.special import lambertw
from sympy import Symbol
import numpy as np


sqrt = np.sqrt
sin = np.sin
cos = np.cos
tan = np.tan
cot = lambda x: 1/tan(x)
acos = np.arccos
asin = np.arcsin
atan = np.arctan
sinh = np.sinh
cosh = np.cosh
tanh = np.tanh
coth = lambda x: 1/tanh(x)
asinh = np.arcsinh
acosh = np.arccosh
atanh = np.arctanh
pi = np.pi
exp = np.exp
e = np.e
log = np.log
LambertW = lambertw
x = Symbol('x')
y = Symbol('y')
j = 1j
I = 1j
