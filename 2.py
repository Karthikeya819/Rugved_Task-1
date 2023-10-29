string = input ("Enter String: -") 
string = sorted(list(string)) 
stri="" 
for i in range(len(string)): 
    stri += string[i] 
print(stri) 
a = set(string) 
for elem in a: 
    print (elem +" - " + str(string.count(elem))) 