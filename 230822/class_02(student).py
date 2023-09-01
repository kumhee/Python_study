class Student :
    def __init__(self, name="학생", studentNumber=0, grade=0):
        self._name = name
        self._studentNumber = studentNumber
        self._grade = grade

    def getName(self) :
        return self._name

    def getGrade(self) :
        return self._grade

    def toString(self) :
        return "이름 : ", self._name, ", 학년 : ", self._grade, ", 학번 : ", self._studentNumber

class Student20(Student):
    gradeNumber = 20
    number = 1

    def __init__(self):
        super().__init__(studentNumber=str(Student20.gradeNumber) + "0" + str(Student20.number), grade=4)
        self.student = Student20.number
        self.zero = "000"
        Student20.number += 1

    def zeroSet(self) :
        num = self.student

        while num // 10 > 0 :
            self.zero = self.zero[0 : len(self.zero)-1]
            num //= 10

        return self.zero

    def toString(self) :
        return "이름 : " + str(super().getName()) + ", 학년 : " + str(super().getGrade()) + ", 학번 : " + str(Student20.gradeNumber) + str(self.zeroSet()) + str(self.student)
        



student20 = Student20()
student21 = Student20()
student22 = Student20()

print(student20.toString())
print(student21.toString())
print(student22.toString())

