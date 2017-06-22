s=input()
s=str(s)
l=[d for d in s]
print(l)
for i in range(0,len(l),2):
	l[i],l[i+1]=l[i+1],l[i]
s="".join(l)
print (s)
