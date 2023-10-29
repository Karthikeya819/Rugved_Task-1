def Fib(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    elif(num==2):
        return 1
    else:
        return Fib(num-1)+Fib(num-2)

n = int(input("Enter n :- "))
for i in range(n):
    print(str(Fib(i)),end=',')