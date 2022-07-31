

amount = int(input())

numbers = []
for i in range(amount):
    numbers.append(int(input()))
    
numbers.sorted()

for i in range(amount):
    print(numbers[i])