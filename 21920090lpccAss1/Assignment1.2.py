
#Accept a file name containing ALP. Open and display it after doing above for each line.


f = open("asm.txt", 'r', encoding="utf-8")
res = ""
ls = []
cnt = 0
for line in f:
    str = line
    for substr1 in str:
        if substr1 != ",":
            res += substr1
        else:
            res += " "

ls = res.split()
for string in ls:
    print(string, end=" ")
print()
print("Count of substrings is: {}".format(len(ls)))

f.close()

# In[ ]:
