# Generate Literal Table with Pool Table
op = {"STOP": "00", "ADD": "01", "SUB": "02", "MULT": "04", "MOVER": "05", "MOVEM": "06", "COMP": "07", "BC": "07",
      "DIV": "08",
      "READ": "09", "PRINT": "10", "START": "01", "END": "01", "ORIGIN": "02", "EQU": "04", "LTORG": "05", "DS": "01",
      "DC": "02",
      "AREG": "01", "BREG": "02", "CREG": "03", "EQ": "01", "LT": "02", "GT": "03", "NE": "04", "ANY": "05"}

f = open("asm.txt", 'r', encoding="utf-8")
res = ""
ls = []
str1 = ""
index = ""
for line in f:
    for string in line:
        if string.isnumeric():
           # print(string)
            index += string
    index = int(index)

    break
#print(index)

for line in f:
    str1 = line
    flag = 0
    for word in line.split():
        if word == "LTORG" or word == "END":
            res += word+" "
            res += str(index)+" "
            index += 1
            flag = 1
    if flag == 1:
        continue

    for substr in str1:
        if substr != ",":
           res += substr
        else:
            res += " "

    index += 1

literal_table_withlc = {}
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

f.close()
#print(ls)

literal_table_withlc = []
f = open("asm.txt", 'r', encoding="utf-8")
cntr = 0

pool_table = []
# print(literal_table_withlc)
for i in range(0,len(ls)):
    if "'" in ls[i] and "=" in ls[i]:
        literal_table_withlc.append([ls[i], 0])
       # print(string)
    elif ls[i].isnumeric():
        continue
    elif ls[i] == "LTORG":
        pool_table.append(cntr)
        index = i
        cntr1 = int(ls[index + 1])+1
        for i in range(cntr, len(literal_table_withlc)):
            tmpLs = literal_table_withlc[cntr]
            # print(tmpLs)
            literal_table_withlc[cntr] = [tmpLs[0], cntr1]
            cntr += 1
            cntr1 += 1
    elif ls[i] == "END":
        if cntr != len(literal_table_withlc):
            pool_table.append(cntr)
        index = i
        cntr1 = int(ls[index + 1])
        for i in range(cntr, len(literal_table_withlc)):
            tmpLs = literal_table_withlc[cntr]
            literal_table_withlc[cntr] = [tmpLs[0], cntr1]
            cntr += 1
            cntr1 += 1

if len(literal_table_withlc) == 0:
    print("No literals in the table")
else:
    print("Literal Table is : ")
    print(literal_table_withlc)
    print("Pool Table is :")
    print(pool_table)

f.close()

# In[ ]:
