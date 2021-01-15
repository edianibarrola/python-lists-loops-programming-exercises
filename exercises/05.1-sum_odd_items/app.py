arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

def sumOdds(numbers):
    total = 0
    for number in numbers:
        if number % 2 != 0:
            total = total + number
    return total

print(sumOdds(arr))

