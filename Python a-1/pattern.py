x=int(input("enter the pattern no."))
y=x**2
print("1",end='')
for i in range(2,x+1):
	if i<=x:
		print(f"0{i}",end='') 
for j in range(y+1,x+y+1):
	print(f"0{j}",end='')
print()
for i in range(x+1,y+2):
	print(f"**{i}",end='')
for i in range(x+2,y+1):
	print(f"0{i}",end='')
