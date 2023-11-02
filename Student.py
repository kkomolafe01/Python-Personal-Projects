# Description of Program: The program will take the exam grades for a given student and print out the average of the exams, so long as exam grades are inputted


class Student:
    def __init__(self, name, exam1 = None, exam2 = None):
        self.__name = str(name)
        self.__exam1 = exam1
        self.__exam2 = exam2

    def getName(self):
        return self.__name

    def getExam1Grade(self):
        return self.__exam1

    def getExam2Grade(self):
        return self.__exam2

    def setExam1Grade(self, exam1grade):
        self.__exam1 = exam1grade

    def setExam2Grade(self, exam2grade):
        self.__exam2 = exam2grade

    def getAverage(self):
        if self.__exam1 == None or self.__exam2 == None:
            print("Some exam grades not available")
            return None
        else:
            return (self.__exam1 + self.__exam2) / 2

    def __str__(self):
        return "Student: " + self.__name + "\n" + "Exam 1: " + str(self.__exam1) + "\n" + "Exam 2: " + str(self.__exam2) + "\n"




