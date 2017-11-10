class Students(object):
    increase = 5 # a variable outside the init which we can use somewhere else
    def __init__(self,first_name,last_name,score):
        self.first_name = first_name
        self.last_name = last_name
        self.score = int(score)

    def show_details(self):
        print(self.first_name + ' '+ self.last_name + ' '+ str(self.score))

    def marks_increase(self):
        end_result = self.score + self.increase
        return print(end_result)

#inheritance new student marks increase by 1.1 and he learns python
class New_student(Students): #inherit Students class but has a new instance variable
    increase = 1.1

    def __init__(self,first_name,last_name,score,language): # we instantiate the initial variables
        super().__init__(first_name,last_name,score) # we use super call initial instances once instead of self.something = something
        self.language = language #here we add our  new instance variable called language


student_new = New_student('Mathew','Donald',18,'Python') #now we add python as the language new student learns
student_new.marks_increase()
student_new.show_details()


student_1 = Students('Mary','Rainberg',90)
student_1.show_details()
student_2 = Students('Peter','Walker',69)
student_2.show_details()
#asumming all increased marks by end of the year with 5,demo purpose
student_new.marks_increase()
student_1.marks_increase()
student_2.marks_increase()
