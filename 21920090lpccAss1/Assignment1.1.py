#Accept a string (1 line in ALP)
#	Replace comma with space. Count and print the substrings
strr = input()
res = ""
for i in strr:
    if i == ',':
        res += " "
    else:
        res += i

print("Formated string is " + res)

arr = res.split(" ")

print("Count of Substrings in line is : " + str(len(arr)))
