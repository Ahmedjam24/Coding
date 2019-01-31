usr=(raw_input())
usr1=raw_input()
usr=usr.split()
usr1=usr1.split()
sum=0
for i in range(int(usr[1])):
    sum=sum+int(usr1[i])
print sum
