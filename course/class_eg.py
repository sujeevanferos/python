class goa:
    name="not set"
    drink=""
    def party(self):
        print("let's party")
    def beach(self):
        print("enjoying the beach")
ramesh=goa()
suresh=goa()
ramesh.name="Ramesh"
print(ramesh.name)
print(suresh.name)
suresh.name="Suresh"
print(suresh.name)
ramesh.drink="yes"
suresh.drink="no"
print("Suresh Drink: ",suresh.drink)