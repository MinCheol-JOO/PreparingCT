# string = 'The Curious Case of Benjamin Button'
# string = 'The last character is a blank '
# string = ' The first character is a blank'

string = input('');
if string == '':
    print(0)
else : 
    words = string.split(' ');

    while '' in words:
        words.remove('');

print(len(words))


