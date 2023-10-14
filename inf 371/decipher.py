import json

##decipher with substitution
 

def decipher(TEXT,table_decipher):
    text = ""
    for LETTER in TEXT:
        if LETTER in table_decipher.keys():
            text = text + table_decipher[LETTER]
        else:
            text = text + LETTER

    return text



##test
#with open("table_decipher.json") as f:
#    table = json.load(f)
#TEXT = "ITSSG, BGW UWBL !"
#text = decipher(TEXT,table)
#print(text)