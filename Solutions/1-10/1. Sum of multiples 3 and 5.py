#No1 - Multiples of 3 and 5 - CodeAvali
#PROMPT: Produce sum of multiples of 3 or 5 below 1,000

sum = 0
for i in range(1,1000):
  multiple = False
  if i % 3 == 0:
    multiple = True
  if i % 5 == 0:
    multiple = True

  if multiple == True: 
    sum += i 

print(sum)