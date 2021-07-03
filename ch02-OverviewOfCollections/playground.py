# Type conversion
message = "Hi there!"
lyst = list(message)
# print(lyst)

toople = tuple(lyst)
# print(toople)

# Create a list using range
lyst = list(range(1, 11, 2))
# print(lyst)

# Cloning and equality
lyst1 = [2, 4, 8]
lyst2 = list(lyst1)

print(f'lyst1 is lyst2: {lyst1 is lyst2}')
print(f'lyst1 == lyst2: {lyst1 == lyst2}')