# Collatz序列
# 主要展示如何定义函数， 并在函数中改变全局变量的值

def Collatz(number):
    global returnValue
    if number%2 == 0:
        returnValue = number//2
    else:
        returnValue = 3*number +1
    
    print(returnValue)

print('Please input a number: ')
returnValue = int(input())

while returnValue != 1:
    Collatz(returnValue)
