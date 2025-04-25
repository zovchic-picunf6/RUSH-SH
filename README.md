# RUSH
Language, which is making for fun and all commands are in Russian.
## Base syntax
### Syntax in RUSH looks like this <br>
```
command *args
```
### example:
```
сум 2 4
```
By now, you can only use integers or variables as arguments (in some specific functions you can use path to file).
### To use variable you need to use prefix "$":
```
сум $послед 5
```

## List of functions
### сум *args
```
сум 12 15
```
output:
```
27
```
returns sum of arguements

### разн arg1 arg2
```
разн 12 10
```
output:
```
2
```
returns difference between numbers

### умнож arg1 arg2
```
умнож 2 3
```
output:
```
6
```
returns product of two numbers

### дел arg1 arg2
```
дел 2 0
```
output:
```
деление на ноль
```
returns quotient of two numbers

### степень arg1 arg2
```
степень 2 5
```
output:
```
32
```
returns __arg1__ in a power of __arg2__
### эхо arg1
```
эхо 121
```
output:
```
121
```
returns __arg1__
### перем arg1 arg2
```
перем число 12
эхо $число
```
output:
```
12
```
creates a variable with name __arg1__ and value __arg2__ or, if there's is already a variable with this name, it'll set it to __arg2__.
