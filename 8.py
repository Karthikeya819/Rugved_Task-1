string = input("Enter String :-")
n = int(input("Enter n :-"))
if(len(string)%n!=0):
    print("String can't be divided into "+str(n)+" Equal Parts.")
else:
    substring=[]
    for i in range(int(len(string)/n)):
        a=""
        for j in range(n):
            a+=string[n*i+j]
        substring.append(a)
    if(len(set(substring))!=1):
        print("String doesn't have same sequence")
    else:
        print(substring)