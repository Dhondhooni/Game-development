from typing_extensions import Self


class Animal:
  def_init_(self, age):
  Self.age = age
    
    def noise(self):
      print("The animal makes a sound")
      
    def showAge(self):
      print("I am", self.age, "years old")
      
class Cat(Animal):
  def_init_(self,age):
    super()._init_(age)
    
  #override "noise" method from "Animal" class
  def noise(self):
    print("The cat says meow")
    
class Dog(Animal)
 def_init_(self,age):
   super()._init_(age)
   
  def noise(self):
    print("The dog says woof")
    
a = Animal(10)
a.noise()
a.ShowAge()

print()

c = Cat(12)
c.noise()

'' '' ''
a.noise() #The noise has changed as we redefined the method
a.showAge() #We can use the "showAge" method from Animal

print()

d = Dog(7)
a.noise()
a.showAge()
'' '' ''
    
    