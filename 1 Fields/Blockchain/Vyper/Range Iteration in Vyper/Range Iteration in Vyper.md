# Range Iteration[](https://docs.vyperlang.org/en/v0.3.7/control-structures.html#range-iteration "Permalink to this headline")

## STOP

Ranges are created using the `range` function. The following examples are valid uses of `range`:
```
for i in range(STOP):
    ...
```
`STOP` is a literal integer greater than zero. `i` begins as zero and increments by one until it is equal to `STOP`.


## START STOP

```
for i in range(start, stop):
    ...
```
`START` and `STOP` are literal integers, with `STOP` being a greater value than `START`. `i` begins as `START` and increments by one until it is equal to `STOP`.

```
for i in range(a, a + N):
    ...
```

`a` is a variable with an integer type and `N` is a literal integer greater than zero. `i` begins as `a` and increments by one until it is equal to `a + N`.
___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]]

