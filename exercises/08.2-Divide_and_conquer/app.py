list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(num_list):
    odd = []
    even = []
    mergeTwoList = []
    for num in num_list:
        if num % 2 != 0:
            odd.append(num)
        else:
            even.append(num)
    mergeTwoList = odd + even
    
    
    return mergeTwoList


print(merge_two_list(list_of_numbers))

