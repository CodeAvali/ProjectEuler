#Sum square diference - first 100 natural numbers

def sum_squares(max):
  sum = 0 
  for i in range(1,max+1):
    sum += (i**2)
  print(sum)
  return sum

def square_sum(max):
  sum = 0
  for i in range(1,max+1):
    sum += i 
  print(sum**2)
  return(sum**2)

print(square_sum(100)-sum_squares(100))