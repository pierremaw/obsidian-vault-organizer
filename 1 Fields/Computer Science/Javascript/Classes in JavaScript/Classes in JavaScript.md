Classes provide a way to define a blueprint for creating objects with specific properties and methods.

A class in JavaScript is defined using the `class` keyword, followed by the name of the class. The body of the class is contained within curly braces and can contain properties, methods, and a constructor method.

Here's an example for a simple class in JavaScript:

```
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  
  sayHello() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }
}

```

In this example, we define a class called `Person` with a constructor method that sets the `name` and `age` properties of a new `Person` object. The class also has a `sayHello` method that logs a greeting to the console.

To create a new instance of the `Person` class, we use the `new` keyword and pass in the required arguments to the constructor method:

```
const john = new Person('John', 30);
john.sayHello(); // logs "Hello, my name is John and I am 30 years old."

```

Classes in JavaScript can also inherit properties and methods from other classes using the `extends` keyword. This allows for a hierarchical class structure, where more specific classes can inherit from more general classes.
!
___
Type: #subtopic 
Topics: [[Computer Science]], [[JavaScript]]

