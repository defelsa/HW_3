
def dict(f):
   list_keys = []
   list_values = []
with open('./task1.txt', 'r') as file:
  data = file.read()
  splitted = data.split('\n')
  results = {}
  for i in list(range(0,len(splitted),2)):
    key, val = splitted[i], splitted[i+1]
    results[key] = val
  print(results)

