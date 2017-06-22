def isIsomorphic(s1,s2):
	d={}
	l1=[x for x in s1]
	l2=[x for x in s2]
	counts1 = dict()
	for i in l1:
		counts1[i] = counts1.get(i, 0) + 1
	counts2 = dict()
	for i in l2:
		counts2[i] = counts2.get(i, 0) + 1
	f=0
	if len(l1)==len(l2):
		for i in range(len(l1)):
			if l1[i] in d:
				val=d.get(l1[i])
				if val == l2[i]:
					pass
				else:
					f=1
					return False
					
			else:
				d[l1[i]]=l2[i]
		if f==0:
			if counts1[l1[i]]==counts2[l2[i]]:
				pass
			else:
				return False
			return True
		else:
			return False
	else:
		return False
if isIsomorphic("foo","baa"):
	print ("isometric")
else:
	print("non isometric")
