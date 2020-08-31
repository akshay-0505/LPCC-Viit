#Generate ST (without LC) and print it.

op = {"STOP": "00", "ADD": "01", "SUB": "02", "MULT": "04", "MOVER": "05", "COMP": "06", "BC": "07", "DIV": "08",
      "READ": "09", "PRINT": "10", "START": "01", "END": "01", "ORIGIN": "02", "EQU": "04", "LTORG": "05", "DS": "01",
      "DC": "02", "AREG": "01", "BREG": "02", "CREG": "03", "EQ": "01", "LT": "02", "GT": "03", "NE": "04", "ANY": "05"}

f = open("asm.txt","r",encoding="utf-8")

res = ""
ls = []
cnt = 0
for line in f :
    str = line
    for substr in str:
        if substr != ",":
            res+=substr
        else:
            res+=" "

ls = res.split()
symbol_list = []

for string in ls:
    if string in op:
        continue
    elif string.isnumeric():
        continue
    elif "'" in string :
        continue
    else:
        symbol_list.append(string)

print("Symbol Table is: ")
print(symbol_list)
