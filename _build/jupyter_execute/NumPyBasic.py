# An Overview of NumPy Arrays

**NumPy** provides numerical back end for nearly every scientific or technical library for Python.It is an important part of the *Scientific Python Ecosystem*. It is an acronym for "Numerical Python".

More information about NumPy is available at [numpy website](http://www.numpy.org).

## Advantages of NumPy

*    NumPy is extremely fast compared to core Python.
*    Many advanced Python libraries such as *SciPy*, *Scikit-Learn* and *Keras* make extensive use of NumPy libraries.
*    NumPy comes with variety of built-in functionalities which in case of core Python, one has to bulit custom code.

## Importing NumPy

In order to use NumPy library, we have to import it in our program. By convention, **numpy module** is imported under the alias **np**

```python
import numpy as np
```
After this we can access functions and classes in the numpy module using np namespace.

## NumPy Array Objects

NumPy's main object is the *homogenous multidimensional array*. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of non-negative integers. In NumPy dimensions are called axes.
	
For example, the coordinates of a point in 3D space $[1, 2, 1]$ has one axis. That axis has 3 elements in it, so we say it has a length of 3. In the example pictured below, the array has 2 axes. The first axis has a length of 2, the second axis has a length of 3.

![A two-dimensional array](Figure\NumpyFig01.png)

NumPy’s array class is called `ndarray`. The more important attributes of an ndarray object are:

|Attributes|Description|
|:---|:---|
|`ndim`|Number of dimensions (axes) of the array|
|`shape`|Number of elements for each dimension of the array. For a matrix with n rows and m columns, shape will be (n,m)|
|`size`|Total number of elements in an array. This is equal to the product of the elements of shape|
|`dtype`|The data type of the elements in the array|
|`nbytes`|Number bytes used to store data|

Let us try to understand the attributes with the following examples.

data = np.array([[1, 2], [3, 4], [5, 6] ])
type(data)

data.ndim

data.shape

data.size

data.dtype

data.nbytes

##  Data Types

 NumPy arrays consist of homogenous data type. The basic data types supported in NumPy are shown below.

|**dtype**|**Variants**|**Description**
|:---|:---|:---
|`int`|`int8`, `int16`, `int32`, `int64`|Integer
|`uint`|`uint8`, `uint16`, `uint32`, `uint64`|Unsigned (non-negative) integers
|`bool`| `bool`|Boolean (True or false)
`float`|`float8`, `float16`, `float32`, `float64`|Floating-point nmbers
|`complex`|`complex64`, `complex128`, `complex256`| complex-valued floating-point number

data = np.array([1, 2, 3, 4], dtype=int)
data

data = np.array([1, 2, 3, 4], dtype=float)
data

data = np.array([1, 2, 3, 4], dtype=complex)
data

Once a NumPy array is created its `dtype` cannot be changed, other than creating a new copy with type-casted array value.

data = np.array([1, 2, 3 ], dtype=float)

data

data.dtype

data = np.array(data, dtype=int)

data.dtype

data

we can do it by `astype` attribute of the `ndarray` class

data = np.array([1, 2, 3 ], dtype=float)

data

data.dtype

data.astype(int)

When computing with NumPy arrays, the data type might get promoted from one type to another, if required by the operation. For example, adding float-valued and complex-valued arrays, the resulting array is a complex-valued array:

d1 = np.array([1, 2, 3 ], dtype=float)
d2 = np.array([1, 2, 3 ], dtype=complex)
d = d1 + d2
d

d.dtype

Depending on the application and its requirement, sometime it is essential to create arrays with appropriate data type, for example, `int` or `complex`. The default datatype is float.

np.sqrt(np.array([-1, 0, 1]))

np.sqrt(np.array([-1, 0, 1], dtype=complex))

## Real and Imaginary Parts

Regardless of the value of the `dtype` attribute, all NumPy array instances have the attributes `real` and `imag` for extracting the real and imaginary parts of the array, respectively:

data = np.array([1, 2, 3], dtype=complex)
data

data.real

data.imag

## Creating Arrays

The functions from the NumPy library that can be used to create arrays of different types:

|Function name|Type of Array|
|:---|:---|
|`np.array`|creates an array from Python list|
|`np.zeros`|Creates an array - with the specified dimension and data type - filled with zeros|
|`np.ones`|Creates an array - with the specified dimension and data type - filled with ones|
|`np.diag`|Creates a diagonal array with specified values along the diagonal and zeros elsewhere|
|`np.arange`|Creates an evenly spaced values between specified start, end and incremental values|
|`np.linspace`|Creates an evenly spaced values between specified start, end, using specified number of elements|
|`np.meshgrid`| Generate coordinate matrices from one dimensional  coordinate vectors|
|`np.random.rand`|Generates an array with random numbers that are uniformly distributed between 0 and 1|

**`np.array`** 
creates an array from a python list

data = np.array([1, 2, 3, 4 ])
data.shape

data = np.array([1, 2, 3, 4])
data, data.ndim, data.shape

To create a two-dimensional array with the same data as in the previous example, we can use a nested Python list:

data = np.array([[1, 2 ], [3 ,4 ] ] )
data.shape

data = np.array([[1, 2 ], [3, 4 ] ])
data, data.ndim, data.shape

### Arrays filled with constant values

**`np.zeros`** and **`np.ones`** <br>
Creat an array - with the specified dimension and data type - filled with zeros and ones respectively.

np.zeros([2,2])

np.zeros([2, 3])

a = np.ones([2, 3])
a

`np.zeros` and `np.ones` functions also accept an optional keyword argument that specifies the data type for the elements in the array. By default, the data type is float64, and it can be changed to the required type by explicitly specify the dtype argument.

data = np.ones(4)
data, data.dtype

data = np.ones(4, dtype=int)
data, data.dtype

An array filled with an arbitrary constant value can be generated by first creating an array filled with
ones, and then multiply the array with the desired fill value.<br>
However, NumPy also provides the function `np.full` that does exactly this in one step.

5.4*np.ones(4)

x1 = 5.4*np.ones(4)
x2 = np.full(4, 5.4)
x1, x2

An already created array can also be filled with constant values using the np.fill function, which takes an array and a value as arguments, and set all elements in the array to the given value. 

np.empty(5)

x1 = np.empty(5)
x1.fill(3.0)
x1

x2 = np.full(5, 3.0)
x2

### Arrays filled with Incremental Sequences

`np.arange` Creates an evenly spaced values between specified **start**, **end** and **incremental values**.
```python
np.arange(start, stop, incremental value)
```

np.arange(1, 10, 0.1)

`np.linspace` Creates an evenly spaced values between specified start, end, using specified number of elements.
```python
np.linspace(start, stop, number of elemnts)
```

np.linspace(1, 10, 50)

### Arrays Filled with Logarithmic Sequences

The function `np.logspace` is similar to `np.linspace`, but the increments between the elements in the array are logarithmically distributed, and the first two arguments are the powers of the optional base keyword argument (which defaults to 10) for the start and end values. 

 np.logspace(0, 2, 5) # 5 data points between 10**0=1 to 10**2=100

### Mesh-grid Arrays

Multidimensional coordinate grids can be generated using the function `np.meshgrid`. Given two one-dimensional coordinate arrays (that is, arrays containing a set of coordinates along a given dimension), we can generate two-dimensional coordinate arrays using the `np.meshgrid` function. 

x = np.array([-1, 0, 1])
y = np.array([-2, 0, 2])
X, Y = np.meshgrid(x, y)

X

Y

To evaluate $(x+y)^2$ at all combinations of values from the $x$ and $y$ arrays above, we can use two-dimensional coordinate arrays X and Y.

Z = (X + Y)^2
Z

### Creating Uninitialized Arrays

To create an array of specific size and data type, but without initializing the elements in the array to any particular values, we can use the function `np.empty`.

np.empty(3, dtype=float)

### Creating Arrays with Properties of Other Arrays

It is often necessary to create new arrays that share properties, such as shape and data type, with another
array. NumPy provides a family of functions for this purpose: `np.ones_like`, `np.zeros_like`, `np.full_like`,
and `np.empty_like`. A typical use-case is a function that takes arrays of unspecified type and size as
arguments, and requires working arrays of the same size and type.

x = np.array([[ 1, 2, 3], [4, 5, 6 ], [7, 8, 9 ] ])
y = np.zeros_like(x)
z = np.ones_like(x)

x

y

z

**`np.random.rand()`** Generates an array with random numbers that are uniformly distributed between 0 and 1.

np.random.rand(3, 3)

### Creating Matrix Arrays

Matrices, or two-dimensional arrays, are an important case for numerical computing. NumPy provides functions for generating commonly used matrices. In particular, the function `np.identity` generates a square matrix with ones on the diagonal and zeros elsewhere:

np.identity(4)

The similar function `numpy.eye` generates matrices with ones on a diagonal

np.eye(3, k=1)

np.eye(3, k=-1)

To construct a matrix with an arbitrary one-dimensional array on the diagonal we can use the `np.diag` function 

np.diag(np.arange(0, 20, 5))

## Indexing and Slicing

|Expression|Description 
|:---|:---
|`a[m]`|Select element at index m, where m is an integer (start counting form 0).
|`a[-m]`|Select the mth element from the end of the list, where m is an integer. The last element in the list is addressed as -1, the second-to-last element as -2, and so on.
|`a[m:n]` | Select elements with index starting at m and ending at n -1 (m and n are integers).
|`a[:]` or `a[:-1]`| Select all elements in the given axis
|`a[:n]`| Select elements starting with index 0 and going up to index n -1 (integer).
|`a[m:]` or `a[m:-1]` |Select elements starting with index m (integer) and going up to the last element in the array.
|`a[m:n:p]`| Select elements with index m through n (exclusive), with increment p.
|`a[::-1]`| Select all the elements, in reverse order.

One Dimensional Array

a = np.arange(0, 10, 1)
a

To select specific elements from this array, for
example the first, the last, and the 5th element we can use integer indexing:

a[0]   # the first element

a[-1]  # the last element

a[4]   ## fifth element or element at index 4

To select a range of elements, say from the *second* to the *second-to-last element*, *selecting every element* and *every second element*, respectively, we can use index slices:

a[1:-1]

a[:]

a[1:-1:2]

To select the *first five* and the *last five elements* from an array, we can use the slices :5 and -5:, since if m or n is omitted in m:n, the defaults are the beginning and the end of the array, respectively

a[:5]

a[-5:]

To reverse the array and select only every second value, we can use the slice ::-2

a[::-2]

### Multidimensionally Arrays

With multidimensional arrays, element selections like those introduced in the previous section can be applied on each axis (dimension). The result is a reduced array where each element matches the given selection rules. 

f = lambda m, n: n+ 10*m
A = np.fromfunction(f, (6,6), dtype=int)
A

We can extract columns and rows from this two-dimensional array using a combination of slice and integer indexing:

A[:,1]   # Second Column

A[1,:]   # Second Row

By applying a slice on each of the array axes, we can extract subarrays. 

A[:3,:3]   #  upper half diagonal block matrix

A[3:,3:]       #lower left off-diagonal block matrix

With element spacing other that 1, submatrices made up from nonconsecutive elements can be extracted:

A[::2, ::2]     #  every second element starting from 0, 0

 A[1::2, 1::3] # every second and third element starting from 1, 1

## NumPy functions for manupulating size and shape of arrays

|Function/Method|Description
|:---|:---
|`np.reshape`| Reshape an N-dimensional array. The total number of elements must remain the same.
|`np.ndarray.flatten`| Create a copy of an N-dimensional array and reinterpret it as a onedimensional array (that is, all dimensions are collapsed into one).
|`np.transpose`| Transpose the array. The transpose operation corresponds to reversing the axes of the array.
|`np.hstack`| Stack a list of arrays horizontally (along axis 1): For example, given a list of column vectors, append the columns to form a matrix.
|`np.vstack`| Stack a list of arrays vertically (along axis 0): For example, given a list of row vectors, append the rows to form a matrix.
|`np.concatenate`| Create a new array by appending arrays after each other, along a given axis.
|`np.append`| Append an element to an array. Creates a new copy of the array.

`np.reshape` Reshape an N-dimensional array. The total number of elements must remain the same.

data = np.array([[1, 2], [3, 4] ])
data

data.shape

data.reshape(1, 4)

data.reshape(4)

`np.ndarray.flatten` Create a copy of an N-dimensional array and reinterpret it as a one dimensional array (that is, all dimensions are collapsed into one).

data = np.array([[1, 2], [3, 4] ])
data

data.flatten()

data.flatten().shape

To create two-dimensional array with the same data, we can use a nested Python list:

data.ndim

data.shape

`np.transpose` Transpose the array. The transpose operation corresponds to reversing the axes of the array.

data = np.arange(9)
data

data = data.reshape([3,3])
data

np.transpose(data)

`np.hstack` Stack a list of arrays horizontally (along axis 1): For example, given a list of column vectors, append the columns to form a matrix.

data = np.arange(5)
data

data = data.reshape(5,1)
data

data = np.hstack([data, data, data, data])
data

`np.vstack` Stack a list of arrays vertically (along axis 0): For example, given a list of row vectors, append the rows to form a matrix.

data = np.arange(1, 5)
data

np.vstack([data, data, data])

`np.concatenate` Create a new array by appending arrays after each other, along a given axis.

a = np.array([[1, 2], [3, 4] ])
b = np.array([[5, 6]])

np.concatenate((a, b), axis=0)

np.concatenate((a, b.T,), axis=1)

`np.append` Append an element to an array. Creates a new copy of the array.

a = np.arange(5)
a

np.append(a, 5)

## Vectorized Expressions

*   The purpose of storing numerical data in arrays is to carry out batch operation  that are applied to all elements in the arrays.
*   Efficient use of vectorized expressions eliminates the need of many explicit `for` loops. 

### Broadcasting

 A $3\times3$ matrix is added to a $1\times 3$ row vector and a $3\times1$ column vector, respectively, and the in both cases the result is a $3\times3$ matrix.<br>
However, the elements in the two resulting matrices are different, because the way the elements of the row
and column vectors are broadcasted to the shape of the larger array is different depending on the shape of
the arrays, according to NumPy’s broadcasting rule.

### Arithmetic Operations
*   The standard arithmetic operations with NumPy arrays perform elementwise operations. Consider, for example, the addition, subtraction, multiplication and division of equal-sized arrays:
	
*   In operations between scalars and arrays, the scalar value is applied to each element in the array, as one
	could expect:
	
*   If an arithmetic operation is performed on arrays with incompatible size or shape, a ValueError	exception is raised:

Operator for elementwise arithmetic operation on NumPy arrays:

|**Operator**|**Operation**
|:---|:---
|+, +=|Addition
|-, -=|Subtraction
|\*,\* = | Multiplication
|/| /=| Division
|//| //=| Integer Division
|\**, \**=| Exponentiation

#### Element wise array-array operation

The standard arithmetic operations with NumPy arrays perform elementwise operations. Consider, for example, the addition, subtraction, multiplication and division of equal-sized arrays:

x = np.array([[1, 2 ], [3, 4 ] ])
y = np.array([[5, 6 ], [7, 8 ] ])

x + y

y - x

x * y

y / x

#### Scalar-array operation
In operations between scalars and arrays, the scalar value is applied to each element in the array, as one could expect:

x * 2

2 ** x

y / 2

If an arithmetic operation is performed on arrays with incompatible size or shape, a ValueError	exception is raised:

x = np.array([[1, 2, 3, 4] ])
x.shape

x = x.reshape(2, 2)
x, x.shape

y = np.array([1, 2 , 3, 4 ])
y.shape

x / y

### Elementwise Functions

In addition to arithmetic expressions using operators, NumPy provides vectorized functions for elementwise evaluation of many elementary mathematical functions and operations. Each of these functions takes a single array (of arbitrary dimension) as input and returns a new array of the same shape, where for each element the function has been applied to the corresponding element in the input array. 

|NumPy function|Description
|:---|:---
|`np.cos, np.sin, np.tan`| Trigonometric functions.
|`np.arccos, np.arcsin. np.arctan`| Inverse trigonometric functions.
|`np.arccosh, np.arcsinh, np.arctanh`| Inverse hyperbolic trigonometric functions.
|`np.arccosh, np.arcsinh, np.arctanh`| Hyperbolic trigonometric functions.
|`np.sqrt`| Square root.
|`np.exp`| Exponential.
|`np.log, np.log2, np.log10`| Logarithms of base e, 2, and 10, respectively.

x = np.linspace(-1, 1, 11)
x

y = np.sin(np.radians(x))
y

np.round(y, decimals=4)

#### Many of the mathematical operator functions operates on two input arrays and returns one array:

*Summary of NumPy functions for elementwise mathematical operations*

|NumPy Function| Description
|:---|:---
`np.add`, `np.subtract`, `np.multiply`, `np.divide`| Addition, subtraction, multiplication and division of two NumPy arrays.
|`np.power `|Raise first input argument to the power of the second input argument (applied elementwise).
|`np.remainder`|The remainder of division.
|`np.reciprocal`|The reciprocal (inverse) of each element.
`np.real, np.imag, np.conj`|The real part, imaginary part, and the complex conjugate of the elements in the input arrays
|`np.sign, np.abs`|The sign and the absolute value.
|`np.floor, np.ceil, np.rint`|Convert to integer values.
|`np.round`|Round to a given number of decimals

np.add(np.sin(x)**2, np.cos(x)**2)

np.sin(x)**2 + np.cos(x)**2

#### Vectorizing a scalar function

import numpy as np

def Heaviside(x):
    if x>1:
        return 1
    else:
        return 0

Heaviside(-1)

Heaviside(1.5)

x = np.linspace(-5, 5, 11)

Heaviside(x)

However, unfortunately this function does not work for NumPy array input.<br>
Using `np.vectorize` the scalar heaviside function can be converted into a vectorized function that
works with NumPy arrays as input:

Heaviside = np.vectorize(Heaviside)
Heaviside(x)

### Aggregate Functions 
NumPy provides another set of functions for calculating aggregates for NumPy arrays, which take *an array as input* and by default return a *scalar as output*. For example, statistics such as averages, standard deviations, and variances of the values in the input array, and functions for calculating the sum and the product of elements in an array, are all aggregate functions.

*A summary of aggregate functions*:

|NumPy Function|Description
|:---|:---
|`np.mean`|The average of all values in the array.
|`np.std`|Standard Deviation.
|`np.var`| Variance.
|`np.sum`|Sum of all the elements.
|`np.prod`|Product of all elements.
|`np.cumsum`|Cumulative sum of all elements.
|`np.cumprod`|Cumulative product of all elements.
|`np.min, np.max`| The minimum / maximum value in an array.
|`np.argmin, np.argmax`| The index of the minimum / maximum value in an array.
|`np.all`| Return True if all elements in the argument array are nonzero.
|`np.any`| Return True if any of the elements in the argument array is nonzero

a = np.random.rand(1, 50)
np.mean(a), np.std(a), np.var(a)

a = np.arange(1, 10, 1)
a

np.sum(a), np.cumsum(a)

np.prod(a), np.cumprod(a)

np.min(a), np.max(a), np.argmin(a), np.argmax(a)

np.all(a), np.any(a)

a = np.array([0, 1, 2, 3, 4, 5 ])
a.all(), a.any()

import numpy as np
data = np.array([[1, 2, 3 ], [4, 5, 6 ], [7, 8, 9 ] ])
data

data.sum()

data.sum(axis=0)

data.sum(axis=1)

### Operations on Arrays

In addition to elementwise and aggregation functions, some operations act on arrays as a whole, and
produce transformed array of the same size. 

*Summary of NumPy functions for array operations*

|**Function**|**Description**
|:---|:---
|`np.transpose, np.ndarray.transpose, np.ndarray.T`|The transpose (reverse axes) of an array.
|`np.fliplr / np.flipud`| Reverse the elements in each row /column.
|`np.rot90 `|Rotate the elements along the first two axes by 90 degrees.
|`np.sort`,`np.ndarray.sort`|Sort the element of an array along a given specified axis (which default to the last axis of the array). The np.ndarray method sort performs the sorting in place, modifying the input array.

data = np.arange(9).reshape(3, 3)
data

np.transpose(data)

data = np.random.randn(1, 2, 3, 4, 5)
data.shape

a = np.random.randn(1, 10)
np.sort(a)

### Matrix and Vector Operations

|`NumPy function `|Description
|:---|:---
|`np.dot`| Matrix multiplication (dot product) between two given arrays representing vectors, arrays, or tensors.
|`np.inner`| Standard deviation.
|`np.cross`| The cross product between two arrays that represent vectors.
|`np.tensordot`| Dot product along specified axes of multidimensional arrays.
|`np.outer`| Outer product (tensor product of vectors) between two arrays representing vectors.
|`np.kron`| Kronecker product (tensor product of matrices) between arrays representing matrices and higher-dimensional arrays.
|`np.einsum`| Evaluates Einstein’s summation convention for multidimensional arrays.

a = np.arange(1, 7)
a

a = a.reshape(3, 2)
a

b = a.reshape(2, 3)
b

c = np.dot(a, b)
c

a@b

# matrix-vector multiplication

a = np.arange(1, 10).reshape(3, 3)
a

b = np.arange(1, 4)
b

np.dot(a, b)

a@b

type(6.6e-16)

For more detail, one may go through the book of

# Bibliography

```{bibliography}
```