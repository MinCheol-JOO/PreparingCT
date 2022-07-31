from audioop import reverse
from re import A


a = int(input())

# a = 2143

# list_a = []
# i =0 
# while(1):
#     if (10**i)<a and (10**(i+1))>a:
#         break;
#     i+=1
    
# a_len = i
# for i in range(a_len+1):
#     c = a%10
#     list_a.append(c)
#     # print(list_a)
#     a/=10;
#     a= int(a)

list_a = []
for i in str(a):
    list_a.append(i)
     

list_a.sort(reverse = True)
for i in list_a:
    print(i,end = '')
print('\n')
