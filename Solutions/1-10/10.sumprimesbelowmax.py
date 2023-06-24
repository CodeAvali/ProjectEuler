#10. Sum of all primes below maximum value 

import math

#function to generate primes below max

def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0: 
            return False;
    return n>1;
  
#summation of primes array

primes = [2]
max = 2000000
for n in range(3, max):
    if isPrime(n):
        primes.append(n)

print(primes)

sum = 0 
for i in range(len(primes)):
  sum += primes[i]

print(sum)
  