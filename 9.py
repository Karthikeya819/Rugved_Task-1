string = input("Enter String to Encrypt :-")
shift = int(input("Enter Shift:-"))
Encrypted=""
for i in range(len(string)):
    if(ord(string[i])==32):
        Encrypted+=" "
    else:
        if(string[i].isupper()):
            Encrypted += chr((ord(string[i]) - shift-65) % 26 + 65)
        else:
            Encrypted += chr((ord(string[i]) - shift - 97) % 26 + 97)
print(Encrypted)