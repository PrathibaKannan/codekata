# your code goes here
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
print("enter the range")
r1=input("")
r2=input("")
r1=int(r1)
r2=int(r2)
c=0
for i in range(r1,r2):
	if isPrime(i):
		print(i)
	
  
