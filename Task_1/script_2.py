def task1(file_name): 
  with open(file_name, 'r') as file: 
    data = file.read() 
  splitted = data.split('\n') 
  results = {} 
  for i in list(range(0, len(splitted), 2)): 
    key, val = splitted[i], splitted[i+1] 
    results[key] = val 
  values = results.values() 
  values_str = " ".join(values) 
  print(values_str) 
 
 
 
task1("task1.txt")