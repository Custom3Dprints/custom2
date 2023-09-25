#1
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

#2
class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    def honor_roll(self): #check if gpa >= 3.5
        if self.gpa >= 3.5:
            return True
        else:
            return False

