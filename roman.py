d={'I':1,'V':5,'X':10}
r=input()
r=str(r)
l=[i for i in r]
if 'V' in l:
	if l.index('V')==1:
		if l[0]=='I':
			print("4")
	else:
		if l.index('V')==0:
			no_of_i=len(l)-1
			print(no_of_i+5)
elif 'X' in l:
	if l.index('X')==1:
		if l[0]=='I':
			print("9")
	else:
		if l.index('X')==0:
			no_of_i=len(l)-1
			print(no_of_i+10)
else:
	print(len(l))                
