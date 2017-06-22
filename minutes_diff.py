hr1=int(input())
min1=int(input())
sec1=int(input())
hr2=int(input())
min2=int(input())
sec2=int(input())
if hr1>hr2:
	h=hr1-hr2
else:
	h=hr2-hr1
if min1>min2:
	m=min1-min2
else:
	m=min2-min1
if sec1>sec2:
	s=sec1-sec2
else:
	s=sec2-sec1
m1=h*60
m=m1+m
print(m)
