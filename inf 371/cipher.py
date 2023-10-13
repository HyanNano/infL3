import json

#cipher with substitution
 

def cipher(text,table_cipher):
    TEXT = ""
    for letter in text:
        if letter in table_cipher.keys():
            TEXT = TEXT + table_cipher[letter]
        else:
            TEXT = TEXT + letter

    return TEXT

#test
with open("table_cipher.json") as f:
    table = json.load(f)
text = "hello, you guys !"
TEXT = cipher(text,table)
print(TEXT)