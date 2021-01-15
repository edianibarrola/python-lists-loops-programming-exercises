
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def filter_r(name):
    if str(name[0]) == "R":
        return name
resulting_names= list(filter(filter_r, all_names ))
print(resulting_names)




