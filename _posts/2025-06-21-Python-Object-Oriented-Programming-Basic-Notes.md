---
title: Python Object Oriented Programming (OOP) Explained with Real Examples--Abstraction to Polymorphism in One Read
permalink: /python-object-oriented-explained-with-examples
date: 2025-06-21
excerpt: When I first learned Python, the biggest mental block I had was understanding classes. Why use them at all when functions just work? But then I realized... OOP wasn’t about writing more code—it was about writing maintainable code.
type: Blog
categories: 
tags: 
status:
---
___

When I first learned Python, the biggest mental block I had was understanding classes. Why use them at all when functions just work? But then I realized... OOP wasn’t about writing more code—it was about writing maintainable code.

In most of the languages, we designed our program around functions. This is called procedure-oriented programming. In object oriented way, data and functionality(method) are wrapped together inside a class. **A class creates new data type and instances of the class are objects**. Understanding this line is important. Consider Class as a design of house. When we build house using the design, we call it object/instance. That means we can create as many houses (objects) we want based on the design (class). Every house might have different number of windows, rooms etc. 

Therefore,  class we can create as many objects just like other variables. For all objects of the a particular class, only data might be different.


There are four fundamental concept in object oriented programming.
1.  Abstraction
2.  Encapsulation
3.  Inheritance
4.  Polymorphism

## Terminology

-   `self` Self represents the current object. Python converts the self into the current object during runtime.  When you create many objects using the class, this `self` variable keeps tracks of individual object's properties. For that reasons, we need to pass this variable when creating class.
-   `Object variable` This variable belongs to the individual objects of the class.
-   `class variable` This is a shared variable for all objects. There is only one copy of this variable. All objects can access this variable and any change of this variable by any objects reflect on all other objects.
-   `Class method` Class method bounds to the class only and has access to the class states.
-   `Static method` Static method is also bound to the class only not object. The difference with class method is that static method does not have access to class variables. It is used as an utility method for class.

### Python Class Toy Example

```python
# Initialize an object class
class Person:
  # A class variable to keep track of number of objects created
  population  = 0;
  # __init__ method is initialization of object. This is the default method
  def __init__(self,name):
	  # self represent the current object that will be passed by the  python itself
    self.name = name  
    # increase population when new object is created
    Person.population +=1
  # method for priting name
  #self should be the first and deafult argument for all methods
  def say_hi(self): 
    print("Hello! I am ",self.name)
  # "@classmethod" is used to define class method
  @classmethod 
  def get_population_count(cls): # class method takes cls as a first parameter
    print("Total population: ", cls.population)
    
# Create a new object
p1 = Person("Shuvangkar")
p1.say_hi()
Person.get_population_count()
#Create another object
p2 = Person("Swati")
p2.say_hi()
Person.get_population_count()

##Output
Hello! I am  Shuvangkar
Total population:  1
Hello! I am  Swati
Total population:  2
```

- `class` creates a template.
- `__init__` runs when a new object is made.
- `self` is used to access things in that object.
- `@classmethod` and `cls` are used to access class-level info like total count.
- Class variables are **shared** by all objects.

## Inheritance

Inheritance is the way of code reusing by acquiring properties from one class to another class. **Car, bus, bike** – all of these come under a broader category called Vehicle. So if we create a vehicle class, and later car class can acquire many properties from common class vehicle. Good point is that any change on the vehicle class will reflects on the car class.

```python
#Base Class
class SchoolMember:
  def __init__(self,name,age):
    self.name = name
    self.age = age
    print("Initialized School Member : ", self.name)

  def getDetails(self):
      print(" Name : ", self.name, " | Age : ",self.age)

# Teacher acquire properties from SchoolMember
class Teacher(SchoolMember):
  def __init__(self,name,age,salary):
    #initialize the base class
    super().__init__(name,age) ##alternate syntax : SchoolMember.__init__(self,name,age)
    
    self.salary = salary
    print("Initialized teacher ", self.name)
  
  def getSalary(self):
    SchoolMember.getDetails(self)
    print("Teacher Salary : ",self.salary)

#Create the object
m1 = SchoolMember("Shuvangkar", 28)
m1.getDetails()

t1 = Teacher("Dr. John",32,5000)
t1.getSalary()
print("Access base class method from subclass")
t1.getDetails()
#output
Initialized SchoolMember :  Shuvangkar
 Name :  Shuvangkar  | Age :  28
Initialized SchoolMember :  Dr. John
Initialized teacher  Dr. John
 Name :  Dr. John  | Age :  32
Teacher Salary :  5000
Access base class method from subclass
 Name :  Dr. John  | Age :  32
```

## Polymorphism and method overriding

The literal meaning of polymorphism is the condition of occurrence in different forms. Like other programming languages, the child classes in Python also inherit methods and attributes from the parent class. We can redefine certain methods and attributes specifically to fit the child class, which is known as **Method Overriding**. Polymorphism allows us to access these overridden methods and attributes that have the same name as the parent class. Python always starts looking for methods in the actual subclass type first, and if it doesn't find anything, it starts looking at the methods in the subclass's base classes.

```python
from math import pi
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length
    #override the base class area method
    def area(self):
        return self.length**2

a = Square(4)
print("Square Area : ",a.area())
```

## Encapsulation

A class is an example of encapsulation. Class bundles data and methods into a single unit and class provides the access to its attribute via method.

We can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single `_` or double `__`.

```python
class Counter:
  def __init__(self):
    self.current = 0;
  
  def increment(self):
    self.current +=1
  def reset(self):
    self.current = 0;
  def getValue(self):
    return self.current;

mycount = Counter()
mycount.increment()
print("Counter : ",mycount.getValue())
mycount.increment()
print("Counter : ",mycount.getValue())
mycount.current = -999 #Accidental assignment, that is not expected
print("Counter : ",mycount.getValue())
#output
Counter :  1
Counter :  2
Counter :  -999
```

From the outside of the counter class, User can access to the `current` attribute and change it. This will create unexpected behavior sometimes. Let’s rewrite the code to prevent such accidental changes.

```python
class Counter:
  def __init__(self):
    #prefix an attribute by double underscore(__)
    #By doing this we cannot access the attribute directly outside of class
    self.__current = 0;
  
  def increment(self):
    self.__current +=1
  def reset(self):
    self.__current = 0;
  def getValue(self):
    return self.__current;

  #Setter function provides the api to change __current value
  def setter(self, value):
    self.__current = value

mycount = Counter()
mycount.increment()
print("Counter : ",mycount.getValue())
mycount.__current = -999 #cannot change the class attribute
print("Counter : ",mycount.getValue())
mycount.setter(100) #private value changin via a method. protectd from direct assignment
print("Counter : ",mycount.getValue())

#output
Counter :  1
Counter :  1
Counter :  100
```


### Private Protected Public

-  Private attributes should only be used by the owner, i.e. inside of the class definition itself. two leading underscores "__” makes the attribute private
-  Protected (restricted) Attributes may be used, but at your own risk. Essentially, they should only be used under certain conditions. single leading underscore “_” marks the attribute as protected
-  Public Attributes can and should be freely used.

```python
class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"
```

### Class Method vs Static method

-   `Class method` Class method bounds to the class only and has access to the class states.
-   `Static method` Static method is also bound to the class only not object. The difference with class method is that static method does not have access to class variables. It is used as an utility method for class.

```python
class Vehicle:
    count = 0
    def __init__(self,model,mileage):
        self.model = model
        self.mileage = mileage
        Vehicle.count +=1
        
    def get_details(self):
        print("Car model: ",self.model," | Mileage: ",self.mileage)
    
    @classmethod
    def total(cls):
        print("Total Car: ", cls.count)

    @staticmethod
    def condition(mileage):
        if(mileage<100):
            print("Condition Good")
        else:
            print("Condition not good")

car1 = Vehicle("RAV4", 130)
car2 = Vehicle("Matrix 2009", 90)
car1.get_details()
car2.get_details()

Vehicle.total()
Vehicle.condition(100)

##############output############
#Car model:  RAV4  | Mileage:  130
#Car model:  Matrix 2009  | Mileage:  90
#Total Car:  2
#Condition not good
```




---
### 👋 About Me
Hi, I’m **Shuvangkar Das**, a power systems researcher with a Ph.D. in Electrical Engineering from Clarkson University. I work at the intersection of power electronics, DER, IBR, and AI — building greener, smarter, and more stable grids. Currently, I’m a Research Engineer at EPRI (though everything I share here reflects my personal experience, not my employer’s views).

Over the years, I’ve worked on real-world projects involving large scale EMT simulation and firmware development for  grid-forming and grid following inverter and reinforcement learning (RL). I also publish technical content and share hands-on insights with the goal of making complex ideas accessible to engineers and researchers.

📺 Subscribe to my [YouTube channel](https://www.youtube.com/@ShuvangkarDas), where I share tutorials, code walk-throughs, and research productivity tips.

<p><strong>Connect with me:<br></strong>
<a href="https://www.youtube.com/@ShuvangkarDas" target="_blank">
    <img src="https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube">
  </a>
  <a href="https://www.linkedin.com/in/ShuvangkarDas" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin">
  </a>
  <a href="https://newsletter.shuvangkardas.com" target="_blank">
    <img src="https://img.shields.io/badge/Newsletter-Subscribe-blue?style=for-the-badge">
  </a>
  <a href="https://twitter.com/shuvangkar_das" target="_blank">
    <img src="https://img.shields.io/badge/Twitter-Follow-blue?style=for-the-badge&logo=twitter">
  </a>
  
  <a href="https://github.com/shuvangkardas" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github">
  </a>
  <a href="https://blog.shuvangkardas.com" target="_blank">
    <img src="https://img.shields.io/badge/Blog-Read-blueviolet?style=for-the-badge">
  </a>
  
</p>

### 📚References




