##Give the table_decipher if we know the table_cipher and vice versa
import json

def tablemaker(tablefilename):
    with open(tablefilename) as infile:
        table = json.load(infile)

    TABLE = dict()

    for key, value in table.items():
        TABLE[value] = key

    name = "tablemaker" + tablefilename
    with open(name, "w") as outfile:
        Table = json.dumps(TABLE)
        outfile.write(Table)

##test
#tablemaker("table_cipher.json")