#7 - 10,001 prime

def create(limit):
  primes = []
  for i in range(2, limit + 1):
    for j in range(2, int(i**0.5) + 1):
      if i%j == 0:
        break
    else:
      primes.append(i)
  return primes

primes = create(500000)
print(primes[10001 - 1])

      