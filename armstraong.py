usr=raw_input()
usr=int(usr)
sum=0
tem=usr
while usr>0:
    rem=usr%10
    sum=sum+(rem**3)
    usr=usr/10
if sum==tem:
    print"yes"
else:
    print'no'
