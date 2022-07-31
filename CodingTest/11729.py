# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def hanoiTower(amountA,start,by,end):
    if amountA == 1:
        print(start,end);
    else:
        hanoiTower(amountA-1,start,end,by);
        print(start, end);
        hanoiTower(amountA-1,by,start,end);

# sum = 1
# for i in range(n - 1):
#     sum = sum * 2 + 1
# print(sum)
a = int(input())

print(2**a-1)
hanoiTower(a, 1, 2, 3)