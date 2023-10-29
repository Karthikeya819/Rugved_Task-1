def Fact(num):
    if(num==0):
        return 1
    else:
        return num*Fact(num-1) 
num = int(input("Enter Number to Find Factorial :- "))
print("Factorial of "+str(num)+" is "+str(Fact(num)))
