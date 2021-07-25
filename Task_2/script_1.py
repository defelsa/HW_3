def average(file_name):
  with open(file_name, 'r') as file:
       values = file.read()
       ints = []
       for value in values:
        try:
           value_int = int(value)
           ints.append(value_int)
        except Exception as e:
         continue 
       print(sum(ints) / len(ints))

average("task2")