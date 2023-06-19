#5 - Smallest perfect multiple - 1 -> 20

def verify(value,max):
  perfect = True
  for i in range(1,max+1):
    if value % i != 0:
      perfect = False
  if perfect:
    return True
  else:
    return False
    
def recursive_solution(value, max):
  while max < 21:
    if verify(value,max):
      print(max, value)
      max += 1
    else:
      value += 2520

  return value

#Method uses knowledge that all solutions will have to be multiples of 2520, Helping to reduce complexity scope 

