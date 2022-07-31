n = int(input())
people = []
for _ in range(n):
    temp = list(input().split())
    people.append((temp[0],int(temp[1]),int(temp[2]),int(temp[3])))

print(people)
people = sorted(people, key = lambda x : (-x[1],x[2],-x[3],x[0]))

for  i in people:
    print(i[0])