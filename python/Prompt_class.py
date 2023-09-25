class Prompt:
    def __init__(self, prompt):
        self.prompt = prompt
    
    def get_input(self):
        self.prompt = input("Enter: ")
        return self.prompt
