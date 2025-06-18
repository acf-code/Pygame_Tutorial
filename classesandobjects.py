#Classes and Objects are very important concepts when it comes to programming
#and is usally called the term Object Oriented Programming(OOP)

#DataTypes:
#1. String - string is text surronded by quotations, readable by humans
#2. Integer - a whole number, between -infinity to infinity
#3. Float - a number with a decimal, between -infinity to infinity
#4. Boolean - True or False

#Examples of Datatypes
#1. "I am 12" - object of the string class
#2. 15
#3. 14.5
#4. False

#Classes are custom datatypes we can define and manipulate
#Object is an instance of a Class
#For example:
#Class Student, Object Andrew
#Class Dog, Object Golden Retriever


#HOW DO WE MAKE A CLASS??????
#We need type lass followed by the name of the class
#The first letter of the name of a class should be captilized

class Candy:
    #we need to create our constructor method,
    #the constructor method sets up our instance variables
    #What is an instance variable?
    #they are variables that describe what a class is
    #for example, a Dog could have an instance variable called color, that tells
    #us what color the dog is
    #What is another instance Variable for a dog?
    #hairAmount, describes how much hair the dog has
    #weight, describes how heavy the dog is

    #To make our constructor method follow this template
    #def __init__(self,parameters*):
    #   instance variables go here
    def __init__(self,sweetnessLevel,color,hardness,shape):
        #to make our instance variable follow this template
        #self.nameofvariable = value
        #if you want to define a value of an instance variable at construction, add the
        #value as a parameter
        self.sweetnessLevel = sweetnessLevel
        self.color = color
        self.hardness = hardness
        self.shape = shape
        #if you want to share the same value for an instance variable across all
        #objects(at least when starting out) have the instance variable equal
        #a set value
        self.dentistApproved = False

    #Next we need to make our methods
    #methods are like functions but inside a class
    #methods define what a class does
    #for example
    #dog class, method called bark(), which barks the dog
    #dog class, method called wagTail(), which wags the tail
    #To make a method, follow this template
    #def methodName(self,parameters*):
    #   you do the code for the method
    # 
    def eatIt(self):
        print("candy was eaten") 

    def explode(self):
        print("candy was exploded")
    #why is there so many self key words? What is it used for?
    #self, lets the class know that following instance variable or methdod is a part of the class

#Let's make some candy objects from our class candy
#To make an object follow this template
#nameOfObject = NameOfClass(parameters*)
kitKat = Candy(6,"brown",4,"rectangle")

skittle = Candy(7,"red",7,"circle")

#If we want to get or change the instance variables from an object do the following template
#nameOfObject.instanceVariable

print(skittle.hardness)
skittle.hardness = 9
print(skittle.hardness)
print(kitKat.sweetnessLevel)

#If we want to call method from an object do the following template
#nameOfObject.method(parameters)

skittle.explode()
kitKat.eatIt()