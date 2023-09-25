class Prompt:
    def __init__(self, prompt):
        self.prompt = prompt

    def get_input(self):
        return self.prompt

prompt = Prompt(float(input("Enter a number: "))).get_input()
