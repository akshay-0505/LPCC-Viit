#Program : Generate ST with LC print it.


# !/usr/bin/env python
# coding: utf-8

# In[69]:


op = {"STOP": "00", "ADD": "01", "SUB": "02", "MULT": "04", "MOVER": "05", "MOVEM": "06", "COMP": "07", "BC": "07",
      "DIV": "08",
      "READ": "09", "PRINT": "10", "START": "01", "END": "01", "ORIGIN": "02", "EQU": "04", "LTORG": "05", "DS": "01",
      "DC": "02",
      "AREG": "01", "BREG": "02", "CREG": "03", "EQ": "01", "LT": "02", "GT": "03", "NE": "04", "ANY": "05"}

f = open("asm.txt", 'r', encoding="utf-8")
res = ""
ls = []
cntr = 0
for line in f:
    str = line
    for substr in str:
        if substr != ",":
            res += substr
        else:
            res += " "

ls = res.split()
print(ls)
symbol_list = []
for string in ls:
    if string in op:
        continue
    elif string.isnumeric():
        continue
    elif "'" in string:
        continue
    elif string in symbol_list:
        continue
    else:
        symbol_list.append(string)

print(symbol_list)

f.close()

# In[73]:


index = ls.index("START")
cntr = int(ls[index + 1])
print(cntr)
cntr -= 1
symbol_list_withlc = {}
for symbol in symbol_list:
    cntr = int(ls[index + 1])
    cntr -= 1
    f = open("asm.txt", 'r', encoding="utf-8")
    for line in f:
        cntr += 1
        if symbol in line:
            symbol_list_withlc[symbol] = cntr
            if "DS" in line:
                symbol_list_withlc[symbol] = cntr
                # symbol_list[symbol_list.index(symbol)]=[symbol,cntr]
                break
            elif "DC" in line:
                symbol_list_withlc[symbol] = cntr
                # symbol_list[symbol_list.index(symbol)]=[symbol,cntr]
                break

    f.close()
print(symbol_list_withlc)

# In[55]:







