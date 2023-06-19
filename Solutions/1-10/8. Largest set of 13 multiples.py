#8. Highest product of adjecent numbers 

f = open("1000digit.txt","r")
data = f.read()

data = str(data)
array = []
for i in range(0,1000):
  array.append(data[i])

highest = 0
lazy_queue = [0] * 13
tail = 0

for i in range(len(data)-1):
  lazy_queue[tail] = data[i]
  tail += 1

  if tail > 12:
    tail = 0

  mult = 1

  #Calculate mult
  for j in range(len(lazy_queue)):
    mult = mult * int(lazy_queue[j])

  if mult > highest:
    highest = mult
    #print(highest, lazy_queue)

print("Answer:", highest)

