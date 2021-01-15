
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

hello = []
#your code go here:
for item in my_list:
    if (type(item) is list):
        hello.append(item)
    if (type(item) is dict):
        hello.append(item)

print(hello)
