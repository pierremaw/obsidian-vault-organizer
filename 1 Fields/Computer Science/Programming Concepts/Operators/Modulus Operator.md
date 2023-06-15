Calculates division remainder.

The modulus operator is a mathematical operator used in programming to calculate the remainder when one integer is divided by another integer. The modulus operator is denoted by the percent sign (%).

## Syntax

The syntax for the modulus operator is as follows:

```
a % b
```

Here, `a` and `b` are integers. The `%` symbol is the modulus operator.

## Examples

Let's look at some examples to understand how the modulus operator works.

### Example 1

Suppose we want to find the remainder when 10 is divided by 3. We can use the modulus operator as follows:

```python
10 % 3  # Output: 1
```

Here, `10` is the dividend, `3` is the divisor, and `1` is the remainder.

### Example 2

Suppose we want to check if a number is even or odd. We can use the modulus operator as follows:

```python
num = 7  

if num % 2 == 0:
	print(f"{num} is even") 
else:     
	print(f"{num} is odd")
```

Here, we first assign the value `7` to the variable `num`. We then use the modulus operator to check if `num` is even or odd. If the remainder when `num` is divided by `2` is `0`, then `num` is even. Otherwise, `num` is odd. In this case, the output would be `7 is odd`.

___
Type: #microtopic 
Topics: [[Computer Science]], [[Programming Concepts]], [[Operators]]

