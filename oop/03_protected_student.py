#name记录名字，score记录成绩
class Students(object):
    def __init__(self,name,score):
        #设为私有(private)变量，不让外部访问，保证了程序代码的健壮性
        #_self.name这种变量外部是可以访问的，当看到这种变量时，“意思是我可以被访问，但是不要随意访问，请把我设置为私有变量”
        '''
        双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量'''
        self.__name = name
        self.__score = score
    def printScore(self):
        print('%s : %s' %(self.__name,self.__score))

    #给外部接口，让其访问self.name,self.score
    def gitName(self):
        return self.__name
    def gitScore(self):
        return self.__score

    #给外部接口，让其可以修改self.score，并对传入的参数进行检查
    def sitScore(self,score):
        #给方法进行检查，避免无效参数
        if 0<= score<= 100:
            self.__score = score
        else:
            #raise用于抛出异常
            raise vaueError('bad score')
student = Students('liwei',90)
student.printScore()
score = int(input("score:"))
student.sitScore(score)
student.printScore()
