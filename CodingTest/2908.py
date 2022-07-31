a,b  = map(int, input().split());
# a = 839
# b= 237


string_A= str(a)
string_B= str(b)
pet_A=string_A[::-1]
pet_B=string_B[::-1]

if pet_A >pet_B:
    print(pet_A)
else:
    print(pet_B)

