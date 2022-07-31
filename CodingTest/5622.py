string = input('');
# string = 'WA'
# string = 'UNUCIC'

dial  = ['ABC', 'DEF','GHI','JKL','MNO', ' PQRS', 'TUV', 'WXYZ']
sum = 0;
for j in range(len(string)): # string의 len만큼 traverse:
    for i in dial :# dial에 해당 값이 있을때까지 돌리는거지
        if string[j] in i:
            sum +=dial.index(i)+3
        
print(sum)

