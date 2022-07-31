permutation =  int(input()) # 몇번쨰 수인지를 출력
# 첫번째 일경우 666
# 두번쨰 일경우 1666
# 세번쨰일경우 2666
# 여섯번쨰일경우 5666
# 일곱번째일경우 6661

main_str = 666
cnt = 0
while True:
    if '666' in str(main_str):
        cnt+=1
    
    if cnt == permutation:
        print(main_str-1)
        break;
    main_str +=1