
def decor_(func):
    def wrapper(list_1):
        list = []
        for el in list_1:
          if isinstance(el, (int, float))  or el.isdigit():
            list.append(float(el))
        func(list)
    return wrapper


@decor_
def list_sum(list_1):
    print(sum(list_1))


a = [1, 5, 4.3, 'dd', '22']
list_sum(a)