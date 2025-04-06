import string

text = "HELLO WOLRD"
character = ""
#print(string.ascii_uppercase)
alphabets = string.ascii_uppercase

for i in range(len(text)):
    for letters in alphabets:
        if text[i] in alphabets:
            character += text[i]
    print(character)