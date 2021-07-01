"""A simple course management system models a student’s information with a name and a set of test scores. This system should be able to create a student object with a given name and a number of scores, all of which will be 0 at startup. The system should be able to access or replace a score at the given position (counting from 0), obtain the number of scores, obtain the highest score, obtain the average score, and obtain the student’s name. In addition, the student object when printed should show the student’s name and scores

Name: Ken Lambert
Score 1: 88
Score 2: 77
Score 3: 100

Define a Student class that supports these features and behavior, and write a short tester function that creates a Student object and runs its methods.
"""

# Create a Student class
class Student():
    
    def __init__(self, name, num_scores):
        self.name = name
        self.scores = num_scores * [0]
        
    # Print a score at a specific position
    def access_score(self, position):
        print(f'Score {position}: {self.scores[position - 1]}\n')
    
    # Replace a score at a specific position
    def replace_score(self, score, position):
        self.scores[position - 1] = score
    
    # Print the highest score of scores
    def highest_score(self):
        # Use max to find the highest score
        highest_num = max(self.scores)
        
        # Index to find the index of the highest score
        idx = self.scores.index(highest_num)
        
        print(f'The highest score is - Score {idx + 1}: {highest_num}\n')
    
    # Print the average of the sum of scores
    def average_score(self):
        average = sum(self.scores) / len(self.scores)
        print(f'The average for all scores is {average}\n')
    
    # Print the students name
    def student_name(self):
        print(self.name)
    
    # Print the students name and all scores
    def __repr__(self):
        print(f'Name: {self.name}')
        
        # Loop through the scores and print out
        for num, score in enumerate(self.scores):
            print(f'Score {num}: {score}')



# Initialize student_1
student_1 = Student('Dean', 4)

# Replace some scores
student_1.replace_score(36, 1)
student_1.replace_score(35, 2)
student_1.replace_score(3, 3)

# Print the highest score
student_1.highest_score()

# Print the average score
student_1.average_score()

# Print string of the object
student_1.__repr__()