usr_n=int(raw_input())
usr_arr=raw_input()
usr_arr=usr_arr.split()
min=int(usr_arr[0])
for i in range(1,usr_n):
    if int(usr_arr[i])<min:
        min=int(usr_arr[i])
print min
