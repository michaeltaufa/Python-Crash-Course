"""
Program Name: A Class to Test (Survey)
Description:
    This program is focused building a Class to be used to test in 
    Chapter 11.
Name: Michael Taufa
Date: 2025-04-22
"""

class AnonymousSurvey:

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_responses(self, new_responses):
        self.responses.append(new_responses)

    def show_results(self):
        print("Survey results: ")
        for response in self.responses:
            print(f"-{response}")
