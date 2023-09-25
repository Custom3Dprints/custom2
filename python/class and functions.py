#Example 1
class dog:
    # returns name
    def get_name(self):
        return self.name, self.age#[-1]
    #
    def __init__(self, Names, Age):
        self.name = Names
        self.age = Age

#print(dog("Roxy", [1, 4, 3, 45]).get_name())


# Example 2
class student:
    def __init__(self, name, age, input):
        self.name = name
        self.age = age
        self.input = input
    def get_grade(self):
        return self.input

s1 = (student("Tim", 19, int(input("Enter num: "))).get_grade())
s2 = student("todd", 19, 75)
s3 = student("ted", 19, 65)


class course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_student(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


Course = course("Science", 2)
Course.add_student(s1)
Course.add_student(s2)

print(Course.get_average_grade())


"""# 1
from class_with_quiz import Question
#ask a multiple choice questions and print if they got it right as a fraction

question_prompts = [
    "What is fav color?\nA. red\nB. green\nC. orange\nD. brown\n\n",
    "My first pet name?\nA. Robin\nB. Roxy\nC. Bob\nD. Dan\n\n",
    "My fav stuff animal?\nA. monkey\nB. bear\nC. milo\nD. koko\n\n"
]
questions = [
    Question(question_prompts[0], "A"),
    Question(question_prompts[1], "B"), 
    Question(question_prompts[2], "D"),
]
#print(Question(questions[0].prompt))

def Answer(questions):
    num = 0
    for question in questions:
        user_answer = input(question.prompt)
        if user_answer.upper() == question.answer:
            num += 1
    print(f"You got a {num}/{len(questions)}")
Answer(questions)"""
"""
#2
from class_with_quiz import Student
student1 = Student("Oscar", "CS", 3.9)
student2 = Student("Bob", "Business", 2.3)

#print(student2.honor_roll()) #checks if student1 is on the honor roll"""