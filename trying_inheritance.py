class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def printname(self):
        print(self.first_name, self.last_name)

person1 = Person("Lupe", "Caireta")
person1.printname()


# class Student(Person):
#     def __init__(self, first_name, last_name):
#         # to add the __init__() function and keep the inheritance of the parent class
#         #if we write another __init__() function it would override the parent's
#         Person.__init__(self, first_name, last_name)
#or it could inherit all methods and properties with the super() function
class Student(Person):
  def __init__(self, first_name, last_name, year):
      super().__init__(first_name, last_name)
      #we add a property and add the parameter <year> in the def part
      self.graduation_year = year
#we add a method called welcome to Student
  def welcome(self):
      print("Welcome", self.first_name, self.last_name, "to the class of", self.graduation_year)

person2 = Student("Alba", "Gosalvez", 2018)
person2.welcome()