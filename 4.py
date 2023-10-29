# Selection-Sort on Strings
string = list(input("Enter String :-"))
for i in range(len(string)):
    smallest = i
    for j in range(i+1,len(string)):
        if(ord(string[j].upper()) < ord(string[smallest].upper())):
            smallest = j
    temp = string[i]
    string[i] = string[smallest]
    string[smallest] = temp

string1 =""
print(string1.join(string))