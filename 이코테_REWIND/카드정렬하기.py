import sys
input_number = int(input())

cards = []
for _ in range(input_number):
    a = int(input())
    cards.append(a)

cards.sort()
distance = 0

for i in range(input_number-1):
    distance = distance+cards[i]+cards[i+1]
    print(distance)