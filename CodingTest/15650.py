
N,M = map(int,input().split())

permutation = []

def permutations(permutation,start):
    if len(permutation) == M:
        print(' '.join(map(str,permutation)))
        return;
        # 그렇지 않을 경우에는
    for i in range(start,N+1) :
        if i in permutation :
            continue;
        permutation.append(i) # 1이 처음에 들어가고
        permutations(permutation,i+1) # i+1을 통해서 permutation에 다시 넣어주고
        # print해준다으 거기에서 pop을 해주고
        # 그다음에 다시 위에서 3을 넣어주는 형식으로 넣어준다
        
        permutation.pop()

        
permutations(permutation,1)
