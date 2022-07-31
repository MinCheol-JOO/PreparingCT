first = int(input())
last = int(input())
# first = 61
# last= 100

prime_set = []


for i in range(first,last+1):
    cnt = 0 
    for j in range(2,i+1):
        if i%j==0:
            cnt+=1
            
            
    if cnt==1:
        prime_set.append(i)

if len(prime_set)>0:
    print(sum(prime_set))
    print(min(prime_set))
else:
    print(-1)