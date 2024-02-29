print()
print("hello world")
print(1+2)
print()
for i in range(5):
    print(i+1)
print()
add=0
a=[]
for i in range(5):
    num=int(input("enter number " + str(i+1)))
    a.append(num)
for i in a:
    add=add+i
print("sum = ",add)