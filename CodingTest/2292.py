# 1 7 19 37
# 6 12 18

dest = int(input());
#dest = 13
cnt = 1;
start = 1
while(start<dest):
    start+=6*cnt;
    cnt+=1;
print(cnt)

