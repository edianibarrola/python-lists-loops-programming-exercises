arr = [45, 67, 87, 23, 5,  32, 60]

#your code below:
new_list = []
index = len(arr)-1
for item in arr:
    new_list.append(arr[index])
    index = index -1

print(new_list)