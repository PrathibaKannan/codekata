n=int(input())
l=[int(d) for d in str(n)]
l1=[]
s=0
a=len(l)
for i in l:
	s=s+(i**a)
if s==n:
	print("amstrong")
else:
  print("not amstrong")
