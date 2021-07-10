class SavingsAccount(object):
    """This class represents a savings account with the owner's name, pin and balance."""
    
    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance
    
    def __lt__(self, other):
        return self.name < other.name
    
    # Other methods, including __eq__
s1 = SavingsAccount('Ken', '1000', 0)
s2 = SavingsAccount('Bill', '1001', 30)

print(s1 < s2, end='\n')
print(s1 > s2, end='\n')

