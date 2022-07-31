inp = int(input())
# inp = 14
start =1;
sum = 0; # 지금까지의 총 개수
count=0; # hierarchy 단락
while(inp>sum):
    sum+=start;
    start+=1; #15를 넘었으니 멈추겠죠?
    count+=1;
denominator = (sum-inp)+1
nominator = count - denominator+1;
if count%2 == 0:
    print('{}/{}'.format(nominator,denominator))
else:
    print('{}/{}'.format(denominator,nominator))


