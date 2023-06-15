- Class methods are methods that are bound to the class and not the instance of the class.
- Class methods can modify the class state, but not the instance state.
- Class methods can be used for factory methods, which are methods that create objects of the class or its subclasses.
- Class methods are defined using the `@classmethod` decorator and take `cls` as the first parameter.
- Class methods can be called by both the class and its instances.

For example:

```python
class Person:
    # A class attribute that counts the number of people
    count = 0

    def __init__(self, name):
        self.name = name
        # Increment the class attribute by 1 for each instance
        Person.count += 1

    # A class method that returns a new person with a default name
    @classmethod
    def create_default(cls):
        return cls("Anonymous")

# Create a person using the class method
p1 = Person.create_default()
print(p1.name) # Anonymous

# Create another person using the constructor
p2 = Person("Alice")
print(p2.name) # Alice

# Print the class attribute
print(Person.count) # 2

# Call the class method using an instance
p3 = p2.create_default()
print(p3.name) # Anonymous

# Print the class attribute again
print(Person.count) # 3
```

___
Type: #microtopic 
Topics: [[Computer Science]], [[Python]], [[Classes in Python]]

