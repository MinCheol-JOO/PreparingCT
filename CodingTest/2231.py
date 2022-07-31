a = int(input())
# a = 216

# 216 = 1+9+8+198

# 1을 정하고 쫙 돌리고, 9정하고 쫙돌리고..

for i in range(1,a+1):
    temp = sum((map(int,str(i))))
    result= i+temp;
    if result == a:
        print(i)
        break;
    if i == a:
        print(0)

    
        