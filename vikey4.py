num2=int(input())
a=0
b=1
c=1
for i in range(num2):
	print(c,end=' ')
	c=a+b
	a=b
	b=c      
