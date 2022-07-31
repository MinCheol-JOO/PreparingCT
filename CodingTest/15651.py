N,M = map(int,input().split())

permutation = [] # 데이터 담을 컨테이너

def permutations(permutation,start):
    if len(permutation) == M:
        print(' '.join(map(str,permutation)))
        return;
    for i in range(start,N+1):
        permutation.append(i)
        permutations(permutation,start)
        permutation.pop()
        # start+=1 #start 값을 넣고 나서 start 값이 1씩 커지게 설계하기 위함
        start+=1

permutations(permutation,1)

