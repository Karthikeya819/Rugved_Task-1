def isAnagram(string1,string2):
    if(len(string1)!=len(string2)):
        return "Not an Anagram"
    count1 = [0]*26
    count2 = [0]*26
    for char in string1:
       count1[ord(char)-65]+=1
    for char in string2:
       count2[ord(char)-65]+=1
    if(count1 == count2):
        return "It's Anagram"


string1 = input("Enter Original Word :-").upper()
string2 = input("Enter Anagram :-").upper()

print(isAnagram(string1,string2))
