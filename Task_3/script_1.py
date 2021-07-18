def time_for_func(func_):
  import time
  
  def wrapper():
        start = time.time()
        func_()
        end = time.time()
        print("Час виконання: {0} секунд.".format(end-start))
  return wrapper

@time_for_func
def aver_list():
  list_1 = []
  while True: 
       n = int(input())
       list_1.append(n) 
       if n == 0: 
            break
  print(sum(list_1)/len(list_1))
