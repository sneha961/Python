w=int(raw_input())
h=int(raw_input())
w1=int(raw_input())
h1=int(raw_input())

wid=w//w1
wid1=w%w1

ht=h//h1
ht1=h%h1
count=0
if(wid1!=0 and ht1!=0):
    count=wid+ht+1

if(wid1==0 and ht1!=0):
    count=wid

if(ht1==0 and wid1!=0):
    count=ht

print(count)
