usr=raw_input()
usr=usr.split()
for i in range (int(usr[0])+1,int(usr[1])):
    if(i%2==0):
        print i
