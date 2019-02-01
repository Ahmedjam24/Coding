usr_n=raw_input()
usr_arr=raw_input()
usr_arr=usr_arr.split()
temp=0
for i in range(0,int(usr_n)):
    if (temp != 0):
        print("\n")
    temp = 1
    print usr_arr[i]
    print" "
    print i
