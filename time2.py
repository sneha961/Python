time=raw_input()
a=(time.split(':'))
hr=int(a[0])
mi=int(a[1])
sec=int(raw_input())
b=sec
a=sec/60
if (a>=61) :
    b=sec%3600
    c=sec//3600
    hr=hr+c
    
div=b//60
add=div+mi
mo=add

if (add>=60):
    dd=add//60
    hr=hr+dd
    mo=add%60

if(hr>23):
    hr=hr%24
hr=str(hr)
mo=str(mo)

print(hr.zfill(2)+":"+mo.zfill(2))

