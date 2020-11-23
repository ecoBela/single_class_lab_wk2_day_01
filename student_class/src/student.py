class Student:

    def __init__(self, input_name, input_cohort):
       self.name = input_name
       self.cohort = input_cohort

    def get_student_to_talk(self, student_name):
        print("I can talk")

    def say_favourite_language(self, language):
        print("I love {language}")
