# Let's start

To start Python, let us begin with some elementary mathematical calculation which otherwise can be done by hand or at best by a simple pocket calculator, if the calculation is big one. This does not require any previous experience of coding nor one need to remember any uncomfortable syntax.


## Python as a calculator

Let us start with writing a few algebric expressions and wait to see how python interpreter responds to it. The syntax is straightforward. One has to just type the expression in the cell and hit `run` or `ctrl+enter` or `shift+enter` from menu bar.

But, before that let us acquiant ourselves with the arithmetic Operators in Python, which are
addition `+`, subtraction `-`, multiplication `*`, division `/`, integer division `//`, modulo operator `%`, power `**`
________________________________________________


|   |   |
|:---:|:---|
| $x+y$  |  Addition |
| $x-y$  | Subtraction  |
|$x*y$   | Multiplication|
|$x/y$   | Division      |
|$x**y$  | Raising $x$ to the power $y$|
|$x//y$  | Integer Division (result is rounded to nearest integer)|
|$x\%y$   | Modulo (the remainder, after x is divided by y)|

2 + 3

4 - 3

4*3

4/3      # Division always returns a floating point number

Anything written after `#` is not implemented by the interpreter and is used to write comment in a code. Writing comment, whenever necessary is considered as a very good coding practise.

If one wants to discard the fractional part and retains the integer, there is another operator `//`.

4//3 # Integer division or floor division discards fractional part and retains only integer

We may find the remainder in a division using modulo `%` operator. This will prove to be very useful in some cases.

8%5

To calculate power, we use `**`

2**5		# '**' represents 2 raised to the power 5

In interactive mode, the last printed expression is assigned to the variable `_`. 

2 + 3

_ + 6

Let us consider another example.

17/7

round(_, 3)

`round()` function restricts the number of places of decimals.

## Rules of algebric operation

1.  Rules of algebric operations are obeyed in Python.
2.  If there are more than one multipliations or divisions, operatons are perforformed from left to right.
3.  Several algebric operations can be combined together to write more complicated algebric operation in Python.
4.  Use parenthesis () to mark things that should be evaluated as unit.

2*6/3 - 5

2*(8-3) - 4*5

(2*3 - 6/2) - (10 - 5)

Operators with mixed type operands convert the integer operand to floating point.

2*3.75/1.4

2*3 + 6

2*(3 + 6)

2*(3 + 6

### Python Modifiers

This is an useful trick available with Python when we want change the value of a variable.

|    |    |    |  
|:---|:---|:---|
|x += 1 | x = x + 1 | update the value of x by adding 1|
|x -= 1 | x = x - 1 | update the value of x by subtracting 1|
|x *= 2.5 | x = x*2.5 | update the value of x by multiplying 2.5 |
|x /= 2.5 | x = x/2.5 | update the value of x by dividing 2.5 |
|x //= 2.5 | x = x//2.5 | update the value of x by dividing 2.5 and round down to an integer|

x = 10
x += 1
x

x = 10
x -= 1
x

x = 10
x *= 5
x

x = 10
x /= 5
x

x = 10
x //= 4
x

### Complex number algebra

The algebric operation with complex numbers are supported by python. A complex number $z = a + jb$ where, $a = 2$ and $b = 3$ can be written as

z = 2 + 3j; z

We can write capital `J` also instead of small `j`. We can further represent `z` as `z = complex(a, b)`.

z = complex(2, 3); z

Addition/ Subtraction/ Multiplication/Division of two complex numbers `z1 = a + jb` and `z2 = c + jd` can be performed.

z1 = 1 + 2j
z2 = 2 + 3j

z = z1 + z2; z

z1 = 5 - 6j
z2 = -2 + 3j

z = z1 - z2; z

z1 = 5 - 6j
z2 = -7 + 4j

z = z1*z2; z

z1 = 1 - 2j
z2 = -3 + 2j

z = z1/z2; z

To extract real and imaginary part from a complex number `z`, we use `z.real` and `z.imag`

z = 1 + 2j
z.real, z.imag

Modulus or absolute value of a complex number $z = A + jb$, given by $\sqrt{(a^2 + b^2)}$ can be calculated.

abs(z) 

## Variable

It is the name of a physical quantity. Say, the temperature at a place is $50^{\circ} C$. We can define a name `temp` and assign the numerical value to it. In that case, the name `temp` is called a variable representing temperature and we write `temp = 50`. Besides being a single number, a variable may represent a set of numbers like vectors or it may represent a matrix also.

### Naming variables

Variable names in Python can contain alphanumerical characters a-z, A-Z, 0-9 and some special characters such as \_ . Normal variable names must start with a letter.

But, *Python keywords cannot be used as variable names*.

### Variable Types

1.  **Integer** - Integer variable can take integer values only (both positive and negative) like 1, 0, -258, but not fractional values like 1.5

2.  **Float** - A floating-point variable can take real numbers like 3.141, $6.63\times10^{-34}$, 1.0. A floating-point variable can take an integer value 1 like 1.0, but an integer variable can not take non-integer value.

3.  **Complex** - A complex variable can take only complex numbers like 1 + 2j or -3.5 - 2.1j

4.  **String** - Any letter, combination of letters i.e. word (may be meaningful or may not be !!!), sentence or numbers within quote represent string.

What is the type of a variable? To know, we use `type` function.



x = 1; type(x)

y = 1.2; type(y)

z = 1 + 2j; type(z)

x = 'a'; type(x)

x = 'Hello !!! Python ...'; type(x)

x = "123"; type(x)

x = 2
y = 3
x*y

### Algebric operations with mixed data type

The general rule -

$$a+b=c$$

|Input($a$)|Input($b$)|Output($c$)|
|:---|:---|:---|
|integer|integer|integer|
|integer|float|float|
|integer|complex|complex|
|float|complex|complex|

x = 2 + 2
x, type(x)

x = 2 + 2.0
x, type(x)

x = 2 + (2 + 2j)
x, type(x)

x = 2.0 + (2 + 2j)
x, type(x)

### Variable assignment

`x = 2` represents variable assignement. We may imagine it to be a kind of a container, labelled as `x`, where its numerical values are stored and whenever, it is required we can retrieve its value. Python is a *dynamically typed language*, so we do not need to specify the type of a variable when we create one. Assigning a value to a new variable creates the variable.

A value can be assigned to several variables simultaneously.

x = y = z = 5
x, y, z

A variable must be assigned before it is used. Say, the variable `a` has not been defined beforehand. If we try to print its value, it will flag a error message.

a

###  Special feature about Python

Assigning the values of two variables in a single statement sequentially. For example,

```python
x, y = 2, 3
```
    

  is equivalent as

```python
x = 2
y = 3
 ```

This feature enables **swapping** the values of two variables in a single statement.

# Swapping variables
print("Before swapping")
x, y = 1, 2
print(x, y, sep="   ")

print("After swapping")

x, y = y, x             # swapping line
print(x, y, sep="   ")

### Type Casting
It is a method of changing a variable from one data type to another. 

x = 1.2; type(x)

x = int(1.2); type(x)

x = complex(1.2)
type(x), x

So, `complex` has converted the type of `1.2`, which is a floating point number and the final representation of `x` is `1.2 + 0j`.

z = 1 + 2j; type(z)

z = float(1 + 2j); type(z)

A `type` conversion converts a variable into more general type. Since, a complex number is more general than real or floating point number, therefore, a floating point variable can be converted to complex variable, but reverse is not possible.

##  Data Type

Data types are usually refer to variables used for storing values. Python does not require any explicit declaration to reserve memory space. Declaration happens automatically when values are assigned to it.

### String Data Type

It is a set of contigious characters represented within quotation mark. It may be single or double quotes.

a_str = "Hello world."
a_str

There is a function called, `type` which tells the interpreter what is the type of variable. For example,

type(a_str)

#### String operation - slicing

We can do slicing of a string. For example,

a_str[0]		# First character of the string

a_str[0:5]	# First five characters of the string

#### String operation - concatenation

Two or more strings can be joined together. For example,

"Computational" + "Physics"

"very" + "hot"

2*"very" + "hot"

### List data type

List is a collection of elements of any type enclosed within square bracket. 

color = ['red', 'blue', 'green']
type(color)

color[0]	# First element of the list

color[0:2]	# First two elements of the list

color.append('yellow')	# adding new element to the list

List elements can be of mixed data type.

a = [1, "First", 1.2, 2+1j]

#### List manipulation or slicing

List manipulation or slicing can be done in the following way -

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a[:-1]	# creates a list starting from first element to the last but one element.

a[2:7]	# creates a list starting from second element to the sixth element.

a[1:9:2]	# creates a list from fisrt element to the eight element jumping two elements

a[::2]		# creates a list from starting to the last number jumping two element

#### Adding, inserting, modifying, and removing elements from lists

Adding an element to an empty list using `append`.

a = []         # an empty list
a.append(1)    # appending '1' to the already empty list
print(a)

a.append(2)    # appending '2' to the list 'a'
print(a)

a.append(3)    # # appending '3' to the list 'a'
print(a)

Elements can be inserted at a particular index location in a list.

fruits = ["apple", "banana", "grapes"]
fruits.insert(1, "mango")
print(fruits)

Lists are mutable. We can modify list by assigning new values to the list.

a = [1, 2, 3]
a[0] = 'First'
print(a)

a[1] = 'Second'
print(a)

a[2] = 'Third'
print(a)

We can remove an elemment from a list.

prime_num = [2, 3, 5, 6, 7, 11, 12, 13]
prime_num.remove(6)
print(prime_num)

del prime_num[5]
print(prime_num)

#### List comprehension using `for` loop

Suppose we create an empty list and want to fill it up by square of the first ten natural numbers. This can be implemented by `for` loop in the following way

s = []  # an empty list
for i in range(1, 11):
	s.append(i**2)
print("s = ",s)

Alternatively, we can write one line code for creating list using

s = [i**2 for i in range(1,11)];s

### Tuple data type

Tuples are like lists except that they can not be modified once created, i.e. they are immutable. In Python, elements within tuples are enclosed within parenthesis () or they can be expressed without parenthesis ().

coordinate = (2,1,4)
print(type(coordinate))
coordinate1 = 1, 2, 5
print(type(coordinate1))

We can unpack the elements of a tuple.

x,y,z = coordinate
print("x = ",x)
print("y = ",y)
print("z = ",z)

### Dictionary data type

Dictionaries are also like lists, except that each element is a \textbf{key-value} pair. The syntax for dictionaries is `{key1 : value1, ...}`.

Parameters = {"Parameter1":1, "Parameter2":2, "Parameter3":3}
type(Parameters)

print(Parameters)
print("Parameter1 = "+str(Parameters["Parameter1"]))
print("Parameter2 = "+str(Parameters["Parameter2"]))
print("Parameter3 = "+str(Parameters["Parameter3"]))

# Assigning new values
Parameters["Parameter1"] = "A"
Parameters["Parameter2"] = "B"

# Adding a new entry
Parameters["Parameter4"] = "D"
print(Parameters)

## Output and Input Statements

`x = 1` is a very simple assignment statement, which states that we have created a variable `x` and assigned a numerical value 1 to it. To display the value of the variable, we use `print()` function.

x = 1
print(x)

`print()` function always displays the current value of the variable.

x = 1
print(x)

x = 2
print(x)

First the value of `x` is assigned the value 1 and `print()` function displays 1. Next, the value of the variable `x` is changed to the value 2 and the value 2 is displayed.

Each `print` statemnt starts in a new line. However, we can print the values in one line.

x = 1
y = 2

print(x, y)

We can separate the variables in the `print` statement by using the code `sep='...'`whatever appears between the quotation marks as a separator, appears between values.

print(x, y, sep=" , ")
print(x, y, sep=" ; ")
print(x, y, sep=" ... ")

We can put some words in the `print` statement.

print('The value of x = ', x, ' and the value of y = ',y)

We can also represent the `print()` in the following way.

print('The value of x = '+str(x)+' and the value of y = '+str(y))

In the `print()`, we have used the property of string concatenation meaning we can add several strings together. `'The value of x = '` and `' and the value of y = '` are two strings, x and y are although numerical variables, we have type casted them to strings.

Say, x = 1.782345. We want the value to be printed to the 3rd places of decimal. This can be done in this way -

x = 1.782345

print('x = %8.3f'%x)
print('x = %0.3f'%x)

What is the difference between two print statements?

There is another way we can represent a `print` statement. This is `format` method, particularly useful when we want to represent a data in tabular format.

x = 10
y = 215.56347

print('{0:5s} {1:5s}'.format('x', 'y'))
print('{0:1d} {1:9.3f}'.format(x,y))

x = 1; print(x)

`x = 1` and the interpreter/computer prints the value 1. If we want to change the value of `x` to some other value, then we have to go to the command line and can make the change. There is an alternative approach, that we can do with `input()` function. If we write `x = input()`, the interpreter/computer will wait for the user to type the value of x.

x = input()

It is always advisable to put some words within parenthesis under quotation mark describing what the input statement is asking for. For example, if we write

x = input("Enter the value of x: ")

`input` statement acts like a `print` statement and prints whatever appears within parenthesis.

But, the surprising fact is that whatever value we enter against the variable is considered as a string by the interprter.

x = input("Enter the value of x: ")
print("The value of x is ", x, " and its data type is ", type(x))

It's quite surprising, since 8 is an integer variable, not a string variable.

x = input("Enter the value of x: ")
print("The value of x is ", x, " and its data type is ", type(x))

So, it is seen that whether it is numerical value or string, `input()` function interpreates it as string. 

If we do some numerical computation and enter numerical values against input statements, then the values will be stored as string and we can not possible do any numerical calculation !!!! It is something like this.

x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

Sum = x + y

print("The sum of ", x, " and ", y, " is ", Sum)

The sum of 8 and 9 is 89 !!! it's rediculus. The reason for this rediculus answer is that both the values of x and y are stored as string and under `+` sign string concatenation has taken place.

So, How to get rid of this problem? The answer is simple. We have to appropriately *typecaste* the variables.

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

Sum = x + y

print("The sum of ", x, " and ", y, " is ", Sum)

and the problem is solved.

## Examples

With this knowledge, we can develop a linear code (a code which proceeds line by line until the last line is reached).

### *How many atoms in the cube?*

A solid cube of aluminum (density 2.7 $gm/cm^3$) has a volume of 0.2 $cm^3$. How many aluminum atoms are contained in the cube?

We know mass = density x volume. So, first of all, let us find out the mass of the aluminum cube.

rho = 2.7
vol = 0.2

mass = rho*vol
print("mass of the cube = ", mass)

We know that one mole of substance contains Avogadro number ($N_A$) of atoms. Weight of one mole of substance is its atomic weight ($W_a$). Therefore, we can write the relation -
\begin{equation}
\frac{N_A}{W_a} = \frac{N}{W}
\end{equation}

Na = 6.023e23
wa = 27
w  = 0.54

N = (w/wa)*Na

print("Number of atoms in the cube =%0.3e "%N)

### *Satellite motion*

Consider a satellite moving around the earth in a circular orbit around earth. The tangential velocity $v$ of the satellite is given by
\begin{equation}
v = \sqrt{\frac{GM_E}{R_E + h}}
\end{equation}

If $T$ is the time-period i.e. time taken to complete one revolution around earth, then, it can shown that height of the satellite above earth should be

\begin{equation}
h = \left(\frac{GM_E T^2}{4\pi^2}\right)^{1/3} - R_E
\end{equation}

where, $G_E = 6.673 \times 10^{-11}N.m^2/kg^2$ is the *universal gravitational constant*, $M_E = 5.98 \times 10^{24} kg$ *mass of the earth*, $R_E = 6.37 \times 10^6 m$ *radius of the earth*.

Let us make an attempt to estimate the height of an *Geosynchronus* satellite.

>A geosynchronous orbit (GEO) is a prograde, low inclination orbit about Earth having a period of 23 hours 56 minutes 4 seconds. A spacecraft in geosynchronous orbit appears to remain above Earth at a constant longitude, although it may seem to wander north and south.

[GEO](https://solarsystem.nasa.gov/basics/chapter5-1/#:~:text=A%20geosynchronous%20orbit%20(GEO)%20is,to%20wander%20north%20and%20south.)

G = 6.673e-11
M = 5.98e24
R = 6.37e6
T = (23*60 + 56)*60 + 4
pi = 3.14

h = (G*M*T**2/(4*pi**2))**(1/3) - R

print("Height of the Geosynchronus satellite = %0.3f"%h,'meter')

## Control Flow

Unlike previous cases where program was executed sequentilly line by line, sometime it is necessary to execute a line only when a specific condition is fulfilled.

The Python syntax uses the keywords `if`, `elif` (else if), `else`for conditional execution of code.

In Python programming language, program blocks are defined by their **indentation level**.

#### Conditional Expressions

|Meaning | Math Symbol | Python Symbol|
|:-----:|:-----:|:-----:|
|Less than | < | <|
|Greater than | > | >|
|Less than or equal | $\le$ | <=|
|Greater than or equal | $\ge$ | >=|
|Equal | = | ==|
|Not equal | $\ne$ | !=|

### if statement


`if` keyword tells the interpreter if the condtion is true, then implement the next line/lines within `if` block, otherwise skip the block.
```
if <condition>:
    <Statement1>
    <Statement2>
    etc.
```

'''
"Air moves from the region of higher pressure to the region of lower pressure." 
Say, if the statement is True or False.
'''
statement = input("type 1 for True and 2 for False: ")

if statement == '1':
    print("Correct answer")

statement = input("type 1 for True and 2 for False: ")

if statement == '1':
    print("Correct answer")

From the above two examples, we find that if the condition is true, then if block is executed and we get answer. But, if the condition is not true, then control does not enter the if block and we do not get any answer.

So, it is always a good idea to incorporate some alternative conditions too. This can be done by adding `elif` (else if) block and `else` block. The structure of the block is

### if-else block

```
if <condition1>:
    <Statement1>     # to be executed if the condition1 is True
elif <condition2>:
    <Statement2>     # to be executed if the condition1 is False and condition2 is True
else:
    <Statement3>     # To be executed if the condition1 and condition2 are False
 ```

`elif` statement tells if the previous condition is not fulfilled, then try this one. `else` tells catch anything, which is not caught by the previous conditions.

Let us modify the above code.

'''
"Air moves from the region of higher pressure to the region of lower pressure." 
Say, if the statement is True or False.
'''
statement = input("type 1 for True and 2 for False: ")

if statement == '1':
    print("Correct answer")
elif statement == '2':
    print("Wrong answer")
else:
    print("You have typed wrong number.")

## Example

### *Odd or even*

To test whether a given number is odd or even.

>A number is even, if it is divisible by 2 and remainder is 0. We can find remainder by modulo operator `%`.

x = float(input("Enter a number: "))

if x%2 == 0:
    print("The number is EVEN.")
else:
    print("The number is ODD.")

### *Prime number*

To find  a set of prime numbers between two given numbers.
>A number which is divisible by 1 and itself is called a **prime number**.

Our approach will be to check whther the number is divisible by all numbers between 1 and the number itself excluding 1 and the number itself.

result = True
num = 70
if num > 1:
    for n in range(2, num):
        if (num % n) == 0:
            result = False
            break

if result == True:
    print(str(num) + " is a Prime number")
else:
    print(str(num) + " is not a prime number.")

## Loops

When same piece of code has to be repeated number of times, we use loop. Here, we shall discuss two varieties -
*   `while`
*   `for`


### `while` loop

`while` condition tells so long condition is true, looping/iteration will continue.

```python
while condition:
       statement
```       

# Rocket blast

time = 5

while time >=0:
    print(time)
    time -= 1
    
print("Blast !!!")

# Sum of first ten natural numbers

num = 1
sum = 0
while num <= 10:
    sum += num
    num += 1
print("sum = "+str(sum))

### Example - *Performing a sum*

Sum the series $$\sum_{k=1}^{100}\frac{1}{k}$$

# By using WHILE loop

# First initialize the variables
num = 0      # number
Sum= 0       # summation

# start looping operation
while num < 100:
    num += 1
    Sum += 1/num

print("Sum = %0.2f"%Sum)

### Example - *The Fibonacci Sequence*

>The Fibonacci numbers are the sequence of integers in which each is the sum of the previous two, with the first two numbers being 1, 1. Thus the first few members of the sequence are 1, 1, 2, 3, 5, 8, 13, 21. 

Calculate the Fibonacci numbers up to 100. 

f1, f2 = 1, 1
while f1<=100:
    print(f1)
    f1,f2 = f2,f1+f2

### `while` loop with `break` 

`while` condition tells the computer to continue looping/iteration if **condition1** is `true` and **condition2** is `false`. Once **condition2** is `true`, looping/iteration will discontinue and control will come out of the `while` block.

```python
while condition1:
      statment         # if condition1 is true
    if condition2:
          break        # if condition2 is true
 ```   

# Tossing a dice

import random

target = 6
no_trial = 10
n = 1

while n < no_trial:
    toss = random.randrange(1, 7)
    print("In throw number "+ str(n) + " the output is "+ str(toss))
    if toss == target:
        print('OK, you can start the game.')
        break
    n += 1

### `while` loop with `continue` 

`while` condition tells the computer to continue looping/iteration. In this looping/iteration, if the **condition2** becomes `true` only that step is skipped, but iteration continue until `while` condition is `true`. 

```python
while condition1:
    statment1
    if condition2:
        continue
 ```         

# Sum of first ten natural numbers not divisible by 3

n = 0
sum = 0
while n <= 9:
    n += 1
    if n%3 == 0:
        continue
    print(n)
    sum += n
print('Sum = ',sum) 

### `for` loop

```python
for item in Sequence:
    indented block of execution
  ```    
looping continues until the last value of the sequence is reached.

vowels = ['a', 'e', 'i', 'o', 'u']

for letter in vowels:
    print("Vowel : %s"%letter)
    print("Within for block")
print("Complete. Outside for block.")

for fruit in ['apple', 'orange', 'banana']:
    print(fruit)

for color in ['red', 'blue', 'green']:
    print(color)

for x in [1, 2, 3]:
    print(x)

for number in [1, 2, 3]:
    print('Yes'*number)

for word in ['Basic', 'Python', 'Programming']:
    print(word)

for i, n in enumerate([-3, -2, -1, 0, 1, 2, 3]):
    print(i, n)

### In built iterator function - `range`

Suppose, we want repeat a particular task, say 10 times or even more, in which case, we can create a `for` loop as follows -

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in a:
    print(num)

Technically, a `for` loop is a loop that runs through the element of a list ('list' will be discussed in section). Consider a list of first ten natural numbers and we want print them one by one. This can be implemented as follows -

There is an inbuilt function called `range` in python which can iterate numbers for the `for` loop.

for i in range(10):
    print(i)

A `range` function starts with 0 and ends with one less than the number mentioned in the `range` function. The syntax of `range` function is

>```range(start, stop, step)```

Suppose we want to generate number from 1 to 10, with step size 2. This can be implemented as follows -

a = [i for i in range(1, 10, 2)]; a

### Example - Emission Lines of Hydrogen Atom

Write a program for calculating the wavelengths of emission lines in the spectrum of the hydrogen atom, based on the Rydberg formula
\begin{equation}
\frac{1}{\lambda}=R\left(\frac{1}{m^2} - \frac{1}{n^2}\right)
\end{equation}

R = 1.097e-2

spectralName = ["Lyman", "Blamer", "Paschen", "Bracket", "Pfund"]
for n in range(1,6):
    print("Series for ",spectralName[n-1])
    print("______________________________")
    print(" ")
    for m in range(n+1, n+5):
        invlambda = R*(1/n**2-1/m**2)
        print(" ",1/invlambda," nm")
    print("______________________________")
    print(" ")

## User defined Function

A function is basically a piece of program code encapsulated with a name such that whenever it is called, it perform the specific job. For example, the factorial of a number may be required to be calculated several times in a program code. We know that the factorial of a number $n$ is defined as the product of all numbers from 1 upto $n$. So, we may write the following piece of code to find the factorial of a number $n$.

fact = 1
num = 5
for i in range(1, num + 1):
	fact *= i
print("Factorial of "+str(num)+" is equal to "+str(fact))

We can encapsulate the above piece of code and define it as a function. 

A function in Python is defined using the keyword `def`, followed by a function name, number of arguments (which are input variables) within parentheses (), and a colon :

So, we can define the factorial function in the following way -

def factorial(n):
	fact = 1
	num = n
	for i in range(1, num + 1):
		fact *= i
	return fact

n = 5
fact = factorial(n)
print("Factorial of "+str(n)+" is equal to "+str(fact))

User defined function can have more than one arguments. For example, if we have a point in cylindrical coordinate ($r,\theta,z$) and we have to calculate the distance between the point and the origin, we can define a function with arguments as $r$, $\theta$ and $z$ and return the value $d$ (distance between the orgin and the point). The simplest way to address this problem is to express $r$ and $\theta$ in terms of cartesian coordinate ($x,y,z$) as follows -

\begin{equation}
\begin{aligned}
	&x = r\cos\theta \\
	&x = r\cos\theta \\
	&z = z
    \end{aligned}
\end{equation}

Applying Pythagorus theorem, distance (d) can be expressed as

\begin{equation}
	d = \sqrt{(r\cos\theta)^2 + (r\sin\theta)^2 + z^2}
\end{equation}
So, the python implementation of the above problem is

from math import *

def func(r, theta, z):
    x = r*cos(theta*pi/180)
    y = r*sin(theta*pi/180)
    d = sqrt(x**2 + y**2 + z**2)
    return d

dist = func(4, 30, 10)
print("Distance = %0.2f"%dist)

## Lambda function

There is an easy way to describe a function when it is relatively of simple type. For example, a function $f(x)=x^2$ may be described as

f = lambda x: x**2
f(2)

### Example - *Rectilinear motion*

A car starts with an initial velocity 5 km/h and moves with an uniform acceleration 50 $km/h^2$. To find the distance covered in any time 't', we use the kinematic relation

\begin{equation}
s = ut + \frac{1}{2}at^2
\end{equation}

where, "s" is the distance covered in time "t", "u" is the initial velocity and "a" is the acceleration. To find the position of the car at every consecuutive hour, we can simply define a function with "s" with "t" as independent variable and "u", "a" as static parameters.

# Basic parameter
u = 10    # initial velocity
a = 50    # uniform acceleration

#Defining a function
s = lambda t: u*t + 0.5*a*t**2

#Evaluation
for n in range(1, 5):
    print("Distance covered in "+str(n)+ " hour = "+str(s(n))+" km.")

Writing comment is a good habit while documenting a code. Anything written after # is not executible by python interpreter. The above result can be expressed in tabular format also.

print("Distance covered:")
print("-----------------------")
print("{0:10s}{1:5s}{2:10s}".format('time', '', 'distance'))
print("-----------------------")
for t in range(5):
    print("{0:2d}{1:15s}{2:5.1f}".format(t, '',s(t)))
print("-----------------------")

## Functions, Packages and Modules

Some large packages are split into smaller subpackages, called **module**. A module within a large package is referred to as `packagename.modulename`.<br>
For example, to calculate the inverse of a matrix, we import **inverse function** from the **linear algebra module** as

```python
    from numpy.linalg import inv
```

### Looking at what a module contains

Once a module is imported, we can list the symbols it provides using the `dir` function:

import math

print(dir(math))

To find the square root of 16, we import `sqrt` function from `math` package.

from math import sqrt
sqrt(4)

### Example

Suppose the position of a point in two-dimensional space is given to us in polar coordinate $r, \theta$ and we want to convert it into Cartesian coordinate $x, y$.

Steps:
1.  Enter the values of $r$ and $\theta$.
2.  Convert the values to Cartesian corodinate using appropriate formulas:
$$x = r\cos\theta:~ y=r\sin\theta$$
3.  Print the result

from math import sin, cos
from numpy import radians

r     = float(input("Enter the value of r : "))
theta = float(input("Enter the value of theta in degree : "))

x = r*cos(radians(theta))
y = r*sin(radians(theta))

print("\n The value of x: " + str(round(x, 2)) + "\n and the value of y: " +str(round(y, 2)))

### Example - *Converting Cartesian corordinates to Polar Coordinates*

Write a program that asks the user for the Cartesian coordinates $x, y$ of a point in two-dimensional space, and calculate and print the corresponding polar coordinates, with the angle $\theta$ given in degrees.

# Converting Cartesian to Polar coordinates
from math import *

x = float(input("Enter the value of x : "))
y = float(input("Enter the value of y : "))

r = sqrt( x**2 + y**2 )
θ = degrees(atan2(y, x))

print("The value of r: " + str(round(r, 2)) + " and the value of θ (degree): " +str(round(θ, 2)))

# Bibliography:
```
{bibliography}
```