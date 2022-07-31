from ast import Is
from logging import PlaceHolder


def IsPrime(num):
    if num == 1:
        return 0;
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True


def PrimeData(Num): # prime array 전달
    Primes = []
    for i in range(2,Num):
        if IsPrime(i):
            Primes.append(i)
    Primes_palin=[]
    for Prime1 in Primes:
        for Prime2 in Primes:
            if Prime1+Prime2 == Num:
                Primes_palin.append([Prime1,Prime2])
    if len(Primes_palin)==1:
        return Primes_palin;
    else:
        maxer = 10000;
        temp_i = 10000;
        temp_j = 4
        for i, j in Primes_palin:
            if abs(i-j)<maxer:
                maxer = abs(i-j);
                temp_i = i;
                temp_j = j;
        return temp_i, temp_j







rep = int(input())
for i in range(rep):
    GoldBachNum = int(input())
    a,b = PrimeData(GoldBachNum)
    print(a,b)
