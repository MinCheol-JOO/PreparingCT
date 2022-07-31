


def fileopen(data, target):
 # 폴더를 읽고 target 이 있으
    with open(data,'r',encoding='UTF8') as file:
    
        text = file.read()
        
        if target in text   :
        
            flag = True
            
        else :
        
            flag = False
 
    return flag
 
 
import os
path = 'H:\파일 하나만 있을경우'
target = int(input('찾을 정수를 입력하세요'))
filelist = os.listdir(path)
new= []
os.chdir('H:\파일 하나만 있을경우')
for i in filelist:
    for j in range(len(filelist)):
        str = '.\\'+i;
        os.chdir(str)
        str2 = path+'\\'+i
        file_list_set = os.listdir(str2)
        if file_list_set[j].endswith('.DAT'):
            new.append(file_list_set[j])
            os.chdir('../')
    for k in file_list_set: # 모든 dat 파일 순회
        flag = fileopen(k,target)
        if flag == True :
            print('찾았습니다. 현재 폴더명은 {j}이고, 파일명은 {}입니다'.format(file_list_set[j]))
            break;
            exit()
    print('못찾았습니다.')

