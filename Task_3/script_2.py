import math 
from math import sqrt 
 
def hypotenuse(a,b): 
   if a != 0 and b != 0: 
            hypo = func(a, b) 
            print("При катетах {} та {}, гіпотенуза дорівнює {}".format(a, b, hypotenuse)) 
   else: 
     print('Довжина катета не може = 0') 
     return hypotenuse 
   
@decor_ 
def hypotenuse(a,b): 
  if a != 0 and b != 0: 
    return math.sqrt(a**2 + b**2) 
  else: 
     print('Довжина катета не може = 0') 
 
hypotenuse_(6, 7)
