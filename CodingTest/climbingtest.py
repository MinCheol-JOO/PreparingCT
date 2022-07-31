# top down 
def climbStairs1(self, n):
    if n==1:
        return 1
    if n==2:
        return 2
    return 
    self.climbStairs1(n-1) + self.climbStairs(n-2)

# bottom up, o(n) space
def climbingStairs2(self,n):
    if n==1:
        return 1
    res = [0 for i in range(n)]

    res[0],res[1]= 1,2
    for i in range(2,n):
        res[i] = res[i-1]+res[i-2]

    return res[-1]


#Bottom Up, constant space
def climbingStairs3(self,n):
    if n == 1:
        return 1
    a,b = 1,2
    for i in range(2,n):
        tmp =b
        b=a+b
        a = tmp
    return b;

# Top down + memorization (list)
def climbingStairs4(self,n):
    if n == 1:
        return 1
    dic = [-1 for i in range(n)]
    dic[0], dic[1] = 1,2
    return self.helper(n-1,dic)

def helper(self,n,dic):
    if dic[n] < 0 :  # 만약 0보다 클 경우에는 바로 memoriziation 된 값을 뱉어준다
        dic[n] = self.helper(n-1,dic) + self.helper(n-2,dic)
    return dic[n]

#Top down + memorization(dict)
def __init__(self):
    self.dic = {1:1,2:2}

def climbstairs(self,n):
    if n not in self.dic:
        self.dic[n] = self.climbStairs(n-1)+ self.climbstairs(n-2)
    return self.dic[n]
