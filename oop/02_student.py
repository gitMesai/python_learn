class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def printStudent(self):
        print('%s : %s' % (self.name,self.score))
    def gitGarde(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'c'

liwei = Student('liwei',90);
liwei.printStudent()
print(liwei.gitGarde())
