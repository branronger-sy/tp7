#1-
from sympy import * 
import math
x=symbols('x')
expr=x**3-6*x**2+5*x+12
deriveF=diff(expr,x)
print(deriveF)
sol=solveset(expr,x)
print("--solutions--")
for i in sol:
    print(i)
print("--fin solutions--")
#2-
x,y=symbols('x,y')
expr=simplify(sin(x)*cos(y)+cos(x)*sin(y))
print(expr)
expr=expand((2*x+3)*4)
print(expr)
#3-
expr=integrate(sin(x)*cos(x))
print(expr)
sol=expr.subs(x,math.pi/2)-expr.subs(x,0)
print(sol)
#4-
expr=4*x+7-3*(x-1)
sol=solveset(expr,x)
print(sol)
#5-je vais utiliser method de l'hopital
expr1=diff(exp(2*x)-1)
expr2=diff(x)
sol=(expr1/expr2).subs(x,0)
print(sol)
