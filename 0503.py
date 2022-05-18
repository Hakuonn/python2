class Circle:
    def __init__(self,radius=1.0):
        self.radius = radius
    
    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

    def get_area(self):
        return self.radius*self.radius*3.14

c1 = Circle()
tmp = c1.get_area()
print(c1.get_area())
print(tmp)

# =====================================
class Point:
    def __init__(self , x= 0  , y = 0):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass   

    def __add__(self):
        pass

    def __mul__(slef):
        pass

p1 = Point(10,20)
p2 = Point()
print(p1.x , ',' , p1.y)
print(p2.x , ',' , p2.y)

# =====================================
class Shape:
    def __init__(self,color='red'):
        self.color = color

    def __str__(self) -> str:
        return 'Hello World'

    def __repr__(self) -> str:
        pass   

class Circle:
    def __init__(self,radius=1.0):
        self.radius = radius

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

    def get_area(self):
        return self.radius*self.radius*3.14

class Rectangle:
    def __init__(self , length = 1.0 , width = 1.0):
        self.length = length
        self.width = width

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

    def get_area(self):
        return self.length * self.width

class Square:
    def __init__(self):
        pass

    def __str__(self) -> str:
        return 'Hello World'

    def __repr__(self) -> str:
        pass


s1 = Shape()
print(s1)

c1 = Circle(9)
print(c1.get_area())

r1 = Rectangle(2,4)
print(r1.get_area())

q1 = Square()
print(q1)

# ==========================================
class Preson:
    def __init__(self , name , male , alter):
        self.name = name
        self.male = male
        self.__alter = alter 
    
    def print_beschreibung() :
        return None

    #getter & setter
    def get_alter(self):
        return self.__alter    

    def set_alter(self , alter):
        self.__alter = alter
    


handsome = Preson('黃天受' , True , 180)
print(handsome.get_alter())
handsome.set_alter(160)
print(handsome.get_alter())


# =======================================
class Author:
    def __init__(self , name , email , gender):
        self.__name = name
        self.__email = email
        self.__gender = gender

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def setEmail(self , email):
        self.__email = email

    def getGender(self):
        return self.__getGender

    def print(self):
        pass

author1 = Author('謝文川' , 'nkust@nkust.edu.tw' , 'm')
print(author1.getEmail())