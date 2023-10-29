text = input("Enter Information:-")
letters =0;
for char in text:
    letters = letters+1 if char.isalpha() else letters
sentences = text.count('.') + text.count('!') + text.count('?')
words = len(text.split())
L = (letters / words) * 100
S = (sentences / words) * 100
CLI = 0.0588 * L - 0.296 * S - 15.8
print(CLI)