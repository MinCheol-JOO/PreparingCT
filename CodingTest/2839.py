from ctypes import sizeof
import os

os.chdir('C:/Users/HYUNSEUNG RHEE/Desktop/주민철/닭/닭파프리카볶음')

path = './'

file_list = os.listdir(path)

file_list_txt = [file for file in file_list if file.endswith('.txt')]

# 2 도리야끼
# 3 닭파프리카볶음
for i in file_list_txt:
    print(i)
    f = open(path+i,'r',encoding='UTF8') 
    line = f.readline()
    list1 = list(line)
    list1[0]='3'
    str1 = ''.join(list1)
    a = open(path+i,'w',encoding='UTF8')
    a.write(str1)
    

print('End!!')