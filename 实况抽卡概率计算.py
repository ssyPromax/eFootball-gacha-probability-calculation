import random
import math
def log(num1,num2):
    return math.log(num2,num1)

a0=int(input('请输入5星球员概率(%):'))
a0=0.01*a0
a=int(input('请输入5星球员数量:'))
b=int(input('请输入高光/黄传/精选球员数量:'))
c=int(input('请输入金币抽取次数:'))
d=int(input('请输入券抽取次数:'))
e=a0*(b/a)
e2=1-e
p0=((e2)**c)*(0.9**d)
p1=((e2)**(c-1)*(c*e))*(0.9**d)+((e2)**c)*(0.9**(d-1)*0.1*d)
p2=((e2)**(c-2)*(c*(c-1)/2)*(e)**2)*(0.9**d) + ((e2)**c)*(0.9**(d-2)*(d*(d-1)/2)*0.01) + ((e2)**(c-1)*(c*e))*((e2)**c)*(0.9**(d-1)*0.1*d)
print('不出的概率:',p0)
print('出一个的概率:',p1)
print('出二个的概率:',p2)
print('出二个以上的概率:',1-p0-p1-p2)
