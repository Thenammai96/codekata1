n=str(input("enter a string"))
l=len(n)
j=l-1
c=''
for i in range(0,l):
    c+=n[j]
    j-=1
print(c)
