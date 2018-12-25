print ("Hello")

n=int(input("Enter number of elements to be inserted:"))
a=[]

for i in range(0,n):
    elem=int(input("Enter element:"))
    a.append(elem)
avg=sum(a)/n
print("Avg of elements in the list",round(avg))