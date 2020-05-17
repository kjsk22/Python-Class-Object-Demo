# this is a demo code for class and objects
class Automobile: #class definition
    """This class is to capture the 
    blueprint or generic attributes applicable for all automobiles"""
    def __init__(self,make,model,wheels): #this is constructor
        self.make = make
        self.model = model
        self.wheel_count = wheels
    def oldnew(self): # this is method
        """This method is to calculate
        if the vehicle is new or old 
        based on manufactured year"""
        if self.model > 2017:
            return "New"
        else:
            return "Old"

car = Automobile("BMW", 2018, 4) #instance of class

#another instance of class
truck = Automobile("Mercedes", 2015, 10)

help(Automobile)

#access method oldnew using object.method syntax
print(car.oldnew())

#access method oldnew using class.method(object) as syntax
print(Automobile.oldnew(car))

print(truck.oldnew())
print(Automobile.oldnew(truck))



