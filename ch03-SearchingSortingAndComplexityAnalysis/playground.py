# def fib(n):
#     if n == 1 or n == 2: return 1
#     else: return fib(n - 1) + fib(n - 2)

# for n in range(1, 33):
#     print(f'{n}: {fib(n)}')




def countdown(i):
    print(i)
    if i == 0: return # Base case
    else:
        countdown(i - 1) # Recursive case

countdown(10)


def greet2(name):
    print(f'How are you, {name}?')

def bye():
    print('Ok bye!')


def greet(name):
    print(f'Hello, {name}')
    greet2(name) # greet is put on hold while greet2 is put on the call stack and executed
    print('Getting ready to say bye...')
    bye() # greet is now put on hold by the bye function which is put on the call stack and executed then greet can finish it's execution finally

greet('Dean')

def fact(n):
    if n == 1: return 1 # Base case
    else:
        return n * fact(n - 1) # Recursive case

print(fact(3)) 