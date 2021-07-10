# def binarySearch(target, sortedLyst):
#     left = 0
#     right = len(sortedLyst) - 1
    
#     while left <= right:
#         midpoint = (left + right) // 2
#         if target == sortedLyst[midpoint]:
#             return midpoint
#         elif target < sortedLyst[midpoint]:
#             right = midpoint - 1
#         else:
#             left = midpoint + 1
#     return - 1

# lyst = [1,2,3,4,5,6,7,8,9]
# print(binarySearch(10, lyst))


# def binarySearch(target, sortedLyst):
#     left = 0
#     right = len(sortedLyst) - 1
#     count = 1
#     while left <= right:
#         midpoint = (left + right) // 2
#         print(f'This is iteration: {count}')
#         print(f'Left:{left} right:{right} midpoint:{midpoint}\n')
        
#         if target == sortedLyst[midpoint]:
#             return midpoint
#         elif target < sortedLyst[midpoint]:
#             right = midpoint - 1
#         else:
#             left = midpoint + 1
        
#         count += 1
#     return - 1


# lyst = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]
# # print(binarySearch(90, lyst))

# lyst2 = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]
# print(binarySearch(44, lyst2))




def binarySearch(target_name, sortedLyst):
    # Alphabet split into 4
    alphaList = ['acbdef', 'ghiklm', 'nopqrs', 'tuvwxyz'] 
    # Return the first character of the name
    targetLetter = target_name[0]
    
    # Return the index of were the targetLetter was found
    left = alphaList.index(targetLetter)
    right = len(alphaList[left]) - 1

    while left <= right:
        midpoint = (left + right) // 2
        if target == sortedLyst[midpoint]:
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return - 1
