def installment(arr=[],*args):
    arr.sort(reverse=True);
    print(arr);
    
    
    l=len(arr);
    z=0;
    for x in range(l):
        z=z+(x+1)*arr[x];
        
    print (z);
a=[];    
p=int(raw_input());
for i in range(0,p):
    m=int(raw_input())
    a.append(m)
installment(a);

