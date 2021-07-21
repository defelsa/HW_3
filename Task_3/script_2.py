import math 
from math import sqrt 

def decor_(f):
    def wrapper(a, b):
        hypotenuse = f(a, b)
        print(f"Катеты {a} {b} гипотенуза {hypotenuse}")
    return wrapper

@decor_
def hypotenuse(a, b): 
  if a != 0 and b != 0: 
    return math.sqrt(a**2 + b**2) 
  else: 
     print('Довжина катета не може = 0') 

hypotenuse(3, 4)
