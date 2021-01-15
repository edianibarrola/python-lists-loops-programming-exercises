chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    empty_list = []
    for item in list1:
        empty_list.append(item)
    for item in list2:
        empty_list.append(item)
    
    
    
    return empty_list
    
print(merge_list(chunk_one, chunk_two))
