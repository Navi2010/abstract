from abc import ABC, abstractmethod

class MATH(ABC):
    @abstractmethod
    def types(self):
        pass
class eighthgrade():
    def types(self):
        print('i am an on level class')
class algebra_1():
    def types(self):
        print('i am k level and GT class')
class geometry():
    def types(self):
        print('u skipped a grade in math')
class algebra_2():
    def types(self):
        print('what are u doing with your life..')

obj = eighthgrade()
obj.types()

obj = algebra_1()
obj.types()

obj = geometry()
obj.types()

obj = algebra_2()
obj.types()