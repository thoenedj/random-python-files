
class Dog:  # Here we are defining a class called Dog. There are no parentheses in the class definition because we're creating this class from scratch. 
    """A simple attempt to model a dog."""  # Here we write a docstring describing what this class does.

    def __init__(self, name, age):  # A function that is part of a class is called a method. 
                                    # The __init__() method is a special method that Python runs automatically whenever we create a new instance based on the Dog class. 
                                    # We define __init__() to have three parameters: self, name, and age. 
                                    # The self parameter is required in the method definition (and it must come before the other parameters) because when Python calls this method later (to create an instance of "Dog"), the method will automatically pass the "self" argument. 
                                    # Every method call associated with an instance automatically passes "self", which is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the class.
                                    # When we make an instance of "Dog", Python will call the __init__() method from the "Dog" class. 
                                    #We'll pass Dog() a name and an age as arguments; self is passed automatically, so we don't need to pass it. 
        """Initialize name and age attributes."""
        self.name = name  # These two variables each have the prefix "self". Any variable prefixed with "self" is available to every method in the class.
                          # We'll also be able to access these variables through any instance created from the class. 
                          # The line "self.name = name" takes the value associated with the parameter "name" and assigns it to the variable "name" which is then attached to the instance being created.
                          # Variables that are accessible through instances like this are called "attributes" 
        self.age = age

    def sit(self): # The "Dog" class has two other methods defined: sit() and roll_over(). Because these methods don't need additional information to run, we just define 
                   # them to have one parameter, "self". The instances we create later will therefore have access to these methods. 
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog('Annabelle', 1) # Here we tell Python to create a dog whose name is Annabelle and whose age is 1. 
                             # When Python reads this line, it calls the __init__() method in "Dog" with the arguments "Annabelle" and "1". 
                             # The __init__() method creates an instance representing this particular dog and sets the "name" and "age" attrinutes using the values provided.
                             # Python then returns an instance representing this dog. We assign that instance to the variable "my_dog".
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# To access attributes of an instance, you use dot notation. We access the value of my_dog's attribute "name" by writing: my_dog.name. 
# This syntax demonstrates how Python find's an attributes value. Here, Python looks at the instance "my_dog" and then finds the attribute "name" associated with "my+dog". 
# This is the same attribute referred to as "self.name" in the class "Dog". 

# After we create an instance from the class "Dog" we can use dot notation to call any method defined in "Dog". 
# Let's make our dog sit and roll over:
my_dog.sit()
my_dog.roll_over()
# To call a method, give the name of the instance and the method you want to call, separated by a dot. When Python reads "my_dog.sit(), it looks for the method "sit()" 
# in the class "Dog" and runs that code. 
# Let's create a second instance of "Dog":
your_dog = Dog("Ruth", 1)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()
# Each dog is a separate instance of "Dog" with its own set of attributes, capable of the same set of actions. 
# Even if we used the same name and age for the second dog, Python would still create a separate instance from the "Dog" class.


another_dog = Dog('Chloe', 13)

another_dog.sit()
another_dog.roll_over()