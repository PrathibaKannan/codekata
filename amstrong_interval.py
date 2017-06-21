def isAmstrong(n):
	l=[int(d) for d in str(n)]
	l1=[]
	s=0
	a=len(l)
	for i in l:
		s=s+(i**a)
	if s==n:
		return 1
a1=int(input())
a2=int(input())
for i in range(a1,a2):
	if isAmstrong(i):
		print(i)
    
    
