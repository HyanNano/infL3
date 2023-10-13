#Give the table_decipher if we know the table_cipher and vice versa
import json

def tablemaker(tablefilename):
    with open(tablefilename) as f:
        table = json.load(f)

    TABLE = dict()

    for key, value in table.items():
        TABLE[value] = key

    name = "tablemaker" + tablefilename
    with open(name, "w") as ff:
        #Table = json.load(ff)
        Table = json.dumps(TABLE)

#test
tablemaker("table_cipher.json")