# """
# Prints the number of calls of a recursive Fibonacci function with problem sizes that double.
# """
# from counter import Counter

# def fib(n, counter):
#     """Count the number of calls of the Fibonacci function."""
#     counter.increment()
#     if n < 3:
#         return 1
#     else:
#         return fib(n - 1, counter) + fib(n - 2, counter)

# problemSize = 2
# print('%12s%15s' % ("Problem Size", 'Calls'))
# for count in range(5):
#     counter = Counter()
#     # The start of the algorithm
#     fib(problemSize, counter)
#     # The end of the algorithm
#     print(problemSize, counter)
#     problemSize *= 2



# Reviewing the finonacci code for a better understanding
def fib(n):
    """Returns the nth Fibonacci number."""
    if n < 3: return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(4))