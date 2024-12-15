from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def move(self):
        pass
class human(animal):
    def move(self):
        print('i walk')
class bird(animal):
    def move(self):
        print('i fly')
class snake(animal):
    def move(self):
        print('i slither')
class fish(animal):
    def move(self):
        print('i swim')

obj = human()
obj.move()

obj = bird()
obj.move()

obj = snake()
obj.move()

obj = fish()
obj.move()