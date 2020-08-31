#!/usr/bin/env python
# coding: utf-8

# In[20]:


#Literal Table With LC without handling LTORG
op={"STOP":"00","ADD":"01","SUB":"02","MULT":"04","MOVER":"05","MOVEM":"06","COMP":"07","BC":"07","DIV":"08",
    "READ":"09","PRINT":"10","START":"01","END":"01","ORIGIN":"02","EQU":"04","LTORG":"05","DS":"01","DC":"02",
     "AREG":"01","BREG":"02","CREG":"03","EQ":"01","LT":"02","GT":"03","NE":"04","ANY":"05"}

f=open("asm.txt",'r',encoding="utf-8")
res=""
ls=[]
cntr=0
for line in f:
    str=line
    for substr in str:
        if substr!=",":
            res+=substr
        else:
            res+=" "

literal_table_withlc={}
ls=res.split()

for string in ls:
    if string in op:
        continue
    elif string.isnumeric():
        continue
    elif "'" in string and "=" in string:
        index=string.index("=")+1
        literal_table_withlc[" " + string[index:] + " "]=0

f.close()


# In[21]:

#!/usr/bin/env python
# coding: utf-8

# In[20]:


#Literal Table With LC without handling LTORG
op={"STOP":"00","ADD":"01","SUB":"02","MULT":"04","MOVER":"05","MOVEM":"06","COMP":"07","BC":"07","DIV":"08",
    "READ":"09","PRINT":"10","START":"01","END":"01","ORIGIN":"02","EQU":"04","LTORG":"05","DS":"01","DC":"02",
     "AREG":"01","BREG":"02","CREG":"03","EQ":"01","LT":"02","GT":"03","NE":"04","ANY":"05"}

f=open("asm.txt",'r',encoding="utf-8")
res=""
ls=[]
cntr=0
for line in f:
    str=line
    for substr in str:
        if substr!=",":
            res+=substr
        else:
            res+=" "

literal_table_withlc={}
ls=res.split()

for string in ls:
    if string in op:
        continue
    elif string.isnumeric():
        continue
    elif "'" in string and "=" in string:
        index=string.index("=")+1
        literal_table_withlc[" " + string[index:] + " "]=0

f.close()


# In[21]:


f=open("asm.txt",'r',encoding="utf-8")
index=ls.index("START")
cntr=int(ls[index+1])
cntr-=1
for line in f:
    cntr+=1

for literal in literal_table_withlc:
    cntr+=1
    literal_table_withlc[literal]=cntr
print("Literal Table")

for literal,lc_counter in literal_table_withlc.items():
    print(literal + " : {}".format(lc_counter))

if len(literal_table_withlc)==0:
    print("No literals in the table")

f.close()


# In[ ]:




f=open("asm.txt",'r',encoding="utf-8")
index=ls.index("START")
cntr=int(ls[index+1])
cntr-=1
for line in f:
    cntr+=1

for literal in literal_table_withlc:
    cntr+=1
    literal_table_withlc[literal]=cntr
print("Literal Table")

for literal,lc_counter in literal_table_withlc.items():
    print(literal + " : {}".format(lc_counter))

if len(literal_table_withlc)==0:
    print("No literals in the table")

f.close()


# In[ ]:



