#12. Large dataset

sum = 0

with open('Large50digit.txt') as data:
    for line in data:
        sum += int(line)

print(sum)

#print(lines)
#value = data.readline()
#sum = sum + int(value)