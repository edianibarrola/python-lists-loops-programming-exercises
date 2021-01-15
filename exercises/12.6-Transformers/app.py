incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]

#Your code go here:
transformedData = []
def my_var(arg):
    transformedData= list(map(lambda x: str(x["name"] + " " + x["lastName"]) , arg))
    return transformedData

print(my_var(incomingAJAXData))