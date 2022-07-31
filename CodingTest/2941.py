Cro_alpha = ['c=', 'c-', 'dz=', 'd-', 's=','z=','lj','nj'];
word = input()

# Croatia 알파벳 숫자?
for i in Cro_alpha:
    word = word.replace(i,'*');

print(len(word))
