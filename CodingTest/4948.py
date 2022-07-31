
# def isPrime(num):
#     if num == 1:
#         return False;
#     else:
#         for i in range(2,int(num**0.5)+1):
#             if num%i == 0:
#                 return False;
#         return True;



# def PrimeCount(num):
#     num_list = [];
#     for i in range(num+1, 2*num+1):
#         if isPrime(i):
#             num_list.append(i);
#     return len(num_list);

# a = 13
# print(PrimeCount(a))
# # a = int(input());
# # while(a !=0):
# #     print(PrimeCount(a))
# #     a = int(input());


# 기능 구현은 했지만, 시간 초과가 떴음

N = 123456*2+1
sieve = [True]*N; # 이것을 통해서 한번에 만들어놓을수있음
for i in range(2, int(N**0.5)+1): # sqrt(n)과 2사이의 모든 수
    if sieve[i]: # 2부터 sqrt(n)이 1이면
        for j in range(2*i,N,i): # i의 2배수부터 i^2까지의 N개를 모두 없앤다
            sieve[j] = False
            # 에라토스테네스의 체

def prime_cnt(val):
    cnt = 0;
    for i in range(val+1, val*2+1):
        if sieve[i]:
            cnt+=1
    print(cnt)
while True:
    val = int(input())
    if val== 0 :
        break;
    prime_cnt(val)
