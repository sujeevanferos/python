# list tuple set
# set cannot be duplicated and it can be modified but we can add or remove
# we cannot modify tuple
# set do not allow duplicates...and it removes duplicates :)

#list
a=[1,2,3,4,5,6]
b=[11,12,13,14,15,16]
a.extend(b)
print(a)

#tuple
print()
c=(1,2,3,4,5)
d=list(c)
print(c)
print(d)

#set
print()
e={1,2,3,4,5,6}
e.pop() #can be add or rmv numbers
print(e)
e.add(10)
print(e)

#dictionay
print()
a={
    "name":"sujeevan",
    "age":"20",
    "location":"sathurukondan",
    "friends":["sivee","seenu","vishan"]
}
print(a["name"])
