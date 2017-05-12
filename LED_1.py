dict={'0' :['a','b','c','d','e','f'] ,'1':['b','c'], '2':['a','b','d','e','g'], '3':['a','b','c','d','g'],'4': ['b','c','f','g'],
      '8':['a','b','c','d','e','f','g'],'9':['a','b','c','f','g'],'7':['a','b','c'],'5': ['a','c','d','f','g'],'6': ['a','c','d','e','f','g']}

n=int(raw_input())
no=(raw_input())
m=no.zfill(n)

l3=[]
for i in m:
    l3.append(i)

count=0
l4=[]
for i in range(n):
    l4.append(dict[l3[i]])

for x in range(0,len(l4)-1):
    l=[a for a in l4[x]+l4[x+1] if (a not in l4[x]) or (a not in l4[x+1])]
    count=count+len(l)

print(count+len(l4[0]))
    

