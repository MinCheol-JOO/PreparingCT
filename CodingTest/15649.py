to, choose_num = map(int,input().split())

permutation_list = []


def permutation(permutation_list):
    if len(permutation_list) == choose_num:
        print(' '.join(map(str,permutation_list)))
        # str 간의 space 하나씩을 넣어준다.
        return;
 
    for i in range(1,to+1): # 1부터 choose_num까지
        if i in permutation_list: # 만약 permutation에 i가 있다면
            continue# 나와주세요!
        permutation_list.append(i)
        permutation(permutation_list)
        permutation_list.pop()


permutation(permutation_list)