#No2 - Even fibonaci below fourmillion sum, 

item1 = 1
item2 = 2
nth = 1
count = 2
exceed = False

while exceed == False:
  swap = item2
  item2 = item1 + item2
  item1 = swap

  if item2 % 2 == 0 and item2 < 4000000:
    count += item2
  elif item2 > 4000000:
    exceed = True 

print(count)