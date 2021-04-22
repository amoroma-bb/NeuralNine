from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():

        """ Interface Method """

class Student(IPerson):

    def __init__(self):
        self.name = 'Basic Student Name'
    
    def person_method(self):
        print('I am a student')
    
class Teacher(IPerson):

    def __init__(self):
        self.name = 'Basic Teacher Name'
    def person_method(self):
        print('I am a teacher')
    
class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == 'Student':
            return Student()
        if person_type == 'Teacher':
            return Teacher()
        else:
            print("invalid Type")
        return -1

if __name__ == '__main__':
    choice = input('what type of person do you want to creat?\n')
    person = PersonFactory.build_person(choice)
    person.person_method()
    print(person.name)
