Number = input ("Enter Number: -") 
Change =0 
Ascend = True 
Hill = True 
Number = list(Number) 
for i in range (1, len(Number)): 
    if(Number[i]<Number[i-1] and Change ==0): 
        Ascend = False 
        Change =1 
    elif(Number[i]<Number[i-1] and Ascend  and Change ==1):
        Hill = False 
        print ("Not an Hill Number") 
    elif(Number[i]>Number[i-1] and not(Ascend) and Change ==1): 
        Hill = False 
        print ("Not a Hill Number") 
    elif(Number[i]==Number[i-1]): 
        Hill = False 
        print ("Not a Hill Number") 
if(Change==0): 
    print ("Not a Hill Number") 
elif(Hill==True): 
    print ("It’s a Hill Number") 