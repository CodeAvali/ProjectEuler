#3. Largest prime number - of 600851475143

import math

number = 600851475143
factors = []

def f(n):
  for i in range(2, int(math.sqrt(n)+1)):
    if n%i == 0:
      factor = True
      for j in range(2, int(math.sqrt(i)+1)):
        if i%j == 0:
          factor = False
          break
        factor = True
      if factor:
        factors.append(i)
  return max(factors)

print(f(number))