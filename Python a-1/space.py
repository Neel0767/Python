x="the quick brown fox jumps over the lazy dog"
a=0
y=x.split()
z=len(y)
for i in range(1,z):
    if y[i] !=" ":
    	a+=1
print(a)