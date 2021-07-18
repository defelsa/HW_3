def decor(f): 
    def wrapper(n): 
        list_1 = f(n) 
        list_ = ' '.join([str(elem) for elem in list_1) 
        print(list_) 
    return wrapper 
 
@decor 
def range_l(n):  
  l = [i for i in range(n+1)]  
  return l  
  
range_list(8)
