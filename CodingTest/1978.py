prime_count= int(input())
# prime_count =4;
prime_number = list(map(int,input().split()))

rescnt = 0 ;
for i in prime_number:
   cnt = 0 ;
   if(i==1): continue;        
   for j in range(2,i+1):
        if(i%j == 0):
            cnt+=1
   if cnt == 1 :
        rescnt +=1

print(rescnt)


        