# 두배열의 원소교체
n,k = map(int,input().split())
a = list(map(int,input().split())) 
b = list(map(int,input().split()))

a.sort()
b.sort(reverse= True)

for i in range(k):
    if a[i]<b[i]:
        a[i],b[i] = b[i],a[i]

    else:
        break #왜냐하면 벗어날경우에는 당연하게, 극히 당연하게, 앞으로는 비교해도 바뀌지 않을것이기 때문이다.
    
print(sum(a))