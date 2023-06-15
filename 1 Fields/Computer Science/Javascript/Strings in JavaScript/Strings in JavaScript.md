A sequence of characters used for text.

## Creating Strings

We can create strings in JavaScript by enclosing text in quotes. There are three types of quotes that can be used to create strings in JavaScript: single quotes (`'`), double quotes (`"`), and backticks (`` ` ``). Here are some examples:

```
const singleQuotes = 'This is a string with single quotes.'; 
const doubleQuotes = "This is a string with double quotes."; 
const backticks = `This is a string with backticks.`;
```

All three of these examples create strings that contain the same text.

## String Methods

In JavaScript, there are many built-in methods that we can use to work with strings. Here are some of the most commonly used string methods:

### `length`

The `length` property returns the length of a string. Here's an example:
```
const str = 'Hello, world!'; console.log(str.length); // logs 13
```

### `indexOf`

The `indexOf` method returns the index of the first occurrence of a specified substring in a string. Here's an example:

```
const str = 'Hello, world!'; console.log(str.indexOf('world')); // logs 7
```

### `slice`

The `slice` method returns a portion of a string. Here's an example:

```
const str = 'Hello, world!'; console.log(str.slice(0, 5)); // logs 'Hello'
```

### `toUpperCase`

The `toUpperCase` method returns a string in all uppercase letters. Here's an example:

```
const str = 'Hello, world!'; console.log(str.toUpperCase()); // logs 'HELLO, WORLD!'
```

## String Concatenation

We can concatenate (join) strings in JavaScript using the `+` operator or the `concat` method. Here are some examples:

```
const str1 = 'Hello';
const str2 = 'world';
const str3 = str1 + ', ' + str2 + '!';
console.log(str3); // logs 'Hello, world!'

const str4 = 'Hello';
const str5 = 'world';
const str6 = str4.concat(', ', str5, '!');
console.log(str6); // logs 'Hello, world!'

```

In both of these examples, we concatenate two strings to create a new string.

## Conclusion

In summary, strings are a fundamental data type in JavaScript used to represent text. We can create strings by enclosing text in quotes, and work with them using a variety of built-in methods. We can also concatenate strings using the `+` operator or the `concat` method. Understanding strings is essential for working with text in JavaScript and building web applications.
___
Type: #subtopic 
Topics: [[Computer Science]], [[JavaScript]]

