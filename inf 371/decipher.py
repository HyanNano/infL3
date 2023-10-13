import json

#cipher with substitution
 

decipher(TEXT,table_decipher){
    text = ""
    for letter in TEXT:
        if letter in table_cipher.keys():
            text = text + table_decipher[letter]
        else:
            text = text + letter

    return text

}

#test
with open("table_decipher.json") as f:
    table = json.load(f)
TEXT = "HELLO, YOU GUYS !"
text = decipher(TEXT,table)
print(text)