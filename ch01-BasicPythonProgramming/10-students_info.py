# Create a Student class

class Student():
    
    def __init__(self, name):
        self.name = name
        self.scores = [0, 0, 0]
        
    def show_name(self):
        print(self.name)

first = Student('Dean')
first.show_name()