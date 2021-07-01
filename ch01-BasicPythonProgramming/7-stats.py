import math 

"""7. Statisticians would like to have a set of functions to compute the median and mode of a list of numbers. The median is the number that would appear at the midpoint of a list if it were sorted. The mode is the number that appears most frequently in the list. Define these functions in a module named stats.py. Also include a function named mean, which computes the average of a set of numbers. Each function expects a list of numbers as an argument and returns a single number."""

def median(lyst):
    """Return the median of a list. If the length of a list is an odd number it will be the middle else it will be the average of the two numbers closest to the midddle"""
    
    # If lyst is an odd length
    if len(lyst) % 2 == 1: return lyst[(len(lyst) // 2)]
    
    # Else even length
    low = lyst[(len(lyst) // 2) - 1]
    high = lyst[(len(lyst) // 2)]
    return (low + high) / 2

print(median([1, 2, 3, 4, 5]))
print(median([1, 2, 3, 4]))

def mode(lyst):
    """Return the number that appears most in the list."""
    # Create a set of one occurance of the numbers
    nums = set(lyst)
    return_value = 0
    top_count = 0
    
    # Iterate over nums and count the occurance of each number in lyst
    for num in nums:
        if lyst.count(num) > top_count:
            return_value = num 
    
    return return_value

print(mode([1,2,3,3,2,5,5,5]))


def mean(lyst):
    return sum(lyst) / len(lyst)

print(mean([1, 2, 3, 4]))
