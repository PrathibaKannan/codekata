def isPrime(n):
	f=0
	if n<2: return 0
	elif n==2: return 1
	else:
		for i in range(2,n):
			if n%i==0:
				f=1
				break
	if f==0:
		return 1
	else:
		return 0
p=int(input())
if isPrime(p):
	print("it's a prime")
else:
	print("it's not a prime")
	
