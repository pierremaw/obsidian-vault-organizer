| Feature | Description                                                                                                                                                                                                                                      |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition                  | BigInt is a built-in object that provides a way to represent whole numbers larger than 2<sup>53</sup> - 1, which is the largest number that can be represented using the Number primitive in JavaScript.                                         |
| Syntax                      | BigInt values can be created by appending the letter "n" to the end of an integer literal or by calling the BigInt() constructor. For example: const bigIntValue = 1234567890123456789012345678901234567890n;                                    |
| Arithmetic operations       | BigInt values can be used in arithmetic operations like addition, subtraction, multiplication, and division using the usual arithmetic operators. For example: const sum = bigIntValue1 + bigIntValue2;                                          |
| Comparison operations       | BigInt values can be compared using the usual comparison operators like <, <=, >, >=, ==, and !=. However, they cannot be compared using the === and !== operators as they perform type coercion.                                                |
| Bitwise operations          | BigInt values can be used in bitwise operations like & (AND), `                                                                                                                                                                                  |
| Conversion                  | BigInt values can be converted to other types using the Number() and String() functions. However, when a BigInt value is converted to a Number, precision can be lost if the value is larger than the maximum safe integer.                      |
| Applications                | BigInt is useful for applications that require handling large integers such as cryptography, financial calculations, and scientific computing. It can also be used to represent the maximum possible length of an array or buffer in JavaScript. |
<!--SR:!2023-05-02,4,270-->

```
const amountIn = 10n ** 18n
```
___
Type: #microtopic 
Topics: [[Computer Science]], [[JavaScript]], [[Objects in Javascript]]

