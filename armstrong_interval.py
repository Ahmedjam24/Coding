usr1=raw_input()
usr1=usr1.split()
arm=[]
for usr in range(int(usr1[0])+1,int(usr1[1])):
    sum = 0
    tem = usr
    while usr > 0:
        rem = usr % 10
        sum = sum + (rem ** 3)
        usr = usr / 10
    if sum == tem:
        arm.append(sum)
        arm.append(' ')
del arm[len(arm)-1]
print str(arm)
