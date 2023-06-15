# Arrays

Arrays are used to store a collection of values of any type in JavaScript. You can access the elements in an array using their index, and add or remove elements as needed.

## Creating an Array

```
const numbers = [1, 2, 3, 4, 5]; const fruits = ['apple', 'banana', 'cherry'];
```

### Accessing Array Elements

```
console.log(numbers[0]); // 1 console.log(fruits[2]); // 'cherry'
```

### Adding and Removing Array Elements

```
fruits.push('orange'); // adds 'orange' to the end of the array fruits.pop(); // removes the last element ('orange') from the array
```

# Sets

`Set` objects are collections of values. A value in the `Set` **may only occur once**; it is unique in the `Set`'s collection. You can iterate through the elements of a set in insertion order.

## Creating a Set

```
const mySet = new Set([1, 2, 3, 4, 5]);

```
### Adding and Removing Values from a Set

```
mySet.add(6); // adds the value 6 to the set mySet.delete(1); // removes the value 1 from the set
```

## Checking if a Value is in a Set

```
console.log(mySet.has(3)); // true console.log(mySet.has(10)); // false
```

# Maps

The **`Map`** object holds key-value pairs and remembers the original insertion order of the keys. Any value (both objects and [primitive values](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)) may be used as either a key or a value.

## Creating a Map

```
const myMap = new Map(); 
myMap.set('name', 'John Doe'); 
myMap.set('age', 30);
```

## Getting the Value of a Key

```
console.log(myMap.get('name')); // 'John Doe' console.log(myMap.get('age')); // 30
```

## Adding and Removing Key-Value Pairs from a Map

```
myMap.set('email', 'john@example.com'); // adds the key-value pair myMap.delete('age'); // removes the key-value pair
```

# Objects

Objects are used to store a collection of key-value pairs in JavaScript. You can access the values in an object using their keys, and add or remove key-value pairs as needed.

## Creating an Object

### Object Initialzer

```
const person = {   name: 'John Doe',   age: 30,   city: 'New York' };
```

### Object() constructor

```
The `Object` constructor** turns the input into an object. Its behavior depends on the input's type.

- If the value is [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null) or [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined), it creates and returns an empty object.
  
- Otherwise, it returns an object of a Type that corresponds to the given value.
  
- If the value is an object already, it returns the value.
```

## Accessing Object Values

```
console.log(person.name); // 'John Doe' console.log(person['age']); // 30
```

## Adding and Removing Object Properties

```
person.email = 'john@example.com'; // adds the 'email' property delete person.city; // removes the 'city' property
```


___
Type: #subtopic 
Topics: [[Computer Science]], [[JavaScript]]

