number = input("Enter Card Number :- ")
s = 0
for i in range(1,len(number)+1):
    if(i%2==0):
        s+=int(number[i-1])
    else:
        if(len(str(int(number[i-1])*2))>1):
            for elem in str(int(number[i-1])*2):
                s+=int(elem)
        else:
            s+=int(number[i-1])*2
if(s%10==0):
    print("Card is Valid")
else:
    print("Card is Not Valid")