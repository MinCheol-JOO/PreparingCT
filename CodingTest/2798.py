# CardAmount = int(input())
# ForCard = int(input())
CardAmount, ForCard = map(int,input().split())


# CardAmount = 5; # 카드의 총개수
# ForCard = 21; # 목표 카드 넘버

arr = list(map(int,input().split()))

result = 0

for i in range(CardAmount):
    for j in range(i+1,CardAmount):
        for k in range(i+2, CardAmount):
            if arr[i]+arr[j]+arr[k] > ForCard:
                continue;
            else:
                result= max(result,arr[i]+arr[j]+arr[k])
