usr_n=int(raw_input())
usr_arr=raw_input()
usr_arr=usr_arr.split()
max=int(usr_arr[0])
for i in range(1,usr_n):
    if int(usr_arr[i])>max:
        max=int(usr_arr[i])
print max
