#4 - Largest palidrome product

def verify(values):
  for i in range(len(values)):
    value = str(values[i])
    set1 = value[0:3]
    set2 = value[3:6]
    empty = ""
    empty = set2[2] + set2[1] + set2[0]
    if empty == set1:
      return values[i]
      break
    
def create(digit):
  values = []
  max = ((10**digit))
  for i in range(900, max):
    for j in range(900, max):
      value = i*j
      values.append(value)
  return values

def insertion_sort(values):
  for i in range(1, len(values)-1):
    elem = values[i]
    j = i - 1
    while j > 0 and values[j] > elem:
      values[j+1] = values[j]
      j = j - 1
    values[j+1] = elem
  return values


values = create(3)
#print(values)
values = insertion_sort(values)
values.reverse()
print(verify(values))
      
    