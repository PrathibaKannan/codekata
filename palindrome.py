a=int(input())
l=[int(d) for d in str(a)]
rl=l[0:len(l)]
l.reverse()
if l==rl:
	print("palindrome")
else:
	print("not palindrome")
