Constructor functions in JavaScript are a way to create objects with specific properties and methods. In this guide, we'll explore how to create and use constructor functions.

# Creating Constructor Functions

A constructor function is a function that is used to create objects with a set of properties and methods. The function is called with the `new` keyword, and it returns a new object with the specified properties and methods.

```javascript
function Person(name, age, gender) {
  this.name = name;
  this.age = age;
  this.gender = gender;
  this.sayHello = function() {
    console.log(`Hello, my name is ${this.name}`);
  };
}

const person = new Person("John", 30, "male");

```

In the example above, we've created a constructor function called `Person` that takes three parameters: `name`, `age`, and `gender`. We've also added a method called `sayHello` to the object using `this`.

When we create a new `Person` object using the `new` keyword, the constructor function sets the `name`, `age`, and `gender` properties, and the `sayHello` method is available on the new object.

# Accessing Constructor Function Properties

Properties on objects created using constructor functions can be accessed using dot notation or square bracket notation.

```javascript
function Person(name, age, gender) {
  this.name = name;
  this.age = age;
  this.gender = gender;
}

const person = new Person("John", 30, "male");

console.log(person.name); // "John"
console.log(person["age"]); // 30

```

# Modifying Constructor Function Properties

Properties on objects created using constructor functions can be modified using dot notation or square bracket notation.

```javascript
function Person(name, age, gender) {
  this.name = name;
  this.age = age;
  this.gender = gender;
}

const person = new Person("John", 30, "male");

person.age = 31;
person["gender"] = "female";

console.log(person.age); // 31
console.log(person.gender); // "female"

```

# Adding Constructor Function Properties

New properties can be added to objects created using constructor functions by simply assigning a value to a property that does not yet exist.

```javascript
function Person(name, age, gender) {
  this.name = name;
  this.age = age;
  this.gender = gender;
}

const person = new Person("John", 30, "male");

person.email = "john@example.com";
person["phone"] = "555-555-5555";

console.log(person.email); // "john@example.com"
console.log(person.phone); // "555-555-5555"

```

___
Type: #microtopic 
Topics: [[Computer Science]], [[JavaScript]], [[Functions in Javascript]]

