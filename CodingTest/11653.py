a = int(input())
# a= 72


# a % b == 0이면
# a /= b 이고, 그걸 쭉 반복
while(a!=1):
    for i in range(2,a+1):
        if a%i == 0:
            
            print(i)
            a/=i
            a= int(a)
            break;


            
