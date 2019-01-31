usr1=raw_input()
usr1=usr1.split()
lower=int(usr1[0])
upper=int(usr1[1])
prime=[]
for num in range(lower+1, upper):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime.extend(str(num))
prime=' '.join(prime)
print prime
