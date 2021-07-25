def decor_(func):
    def wrapper(n):
      m_list = func(n)
      return list(map(str, m_list))
    return wrapper

@decor_
def m_list(n):
    list_1 = [el for el in range(n + 1)]
    return list_1

m_list(8)
