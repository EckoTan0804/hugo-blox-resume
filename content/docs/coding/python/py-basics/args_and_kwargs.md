---
linktitle: ''
summary: ''
weight: 11
title: args and kwargs
date: 2020-07-06
draft: false

authors:
- admin
tags:
- Python
- Basics
categories:
- Coding
toc: true
profile: false
reading_time: true
share: true
featured: true
comments: true
disable_comment: false
commentable: true
editable: false
header:
  caption: ''
  image: ''
---

## Passing multiple arguments to a function

`*args` and `**kwargs` allow you to pass multiple arguments or keyword arguments to a function. 

- `args `will collect extra positional arguments as a tuple because the parameter name has a `*` prefix.
- `kwargs `will collect extra keyword arguments as a dictionary because the parameter name has a `**` prefix

For example, we neede to take a **various** numbers of arguments and compute their sum.


The first way is often the most intuitive for people that have experience with collections: simply pass a `list` or a `set` of all the arguments to your function.


```python
def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3]
my_sum(list_of_integers)
```


    6

This implementation works, but whenever you call this function you’ll also need to create a list of arguments to pass to it. This can be inconvenient, especially if you don’t know up front all the values that should go into the list. 🤪

This is where `*args` can be really useful, because it allows you to pass a varying number of positional arguments.


```python
def my_sum(*args):
    result = 0
    # Iterating over the python `args` tuple
    for x in args:
        result += x
    return result

# *args = 1, 2, 3
# -> args = (1, 2, 3)
my_sum(1, 2, 3)
```


    6


```python
def print_args(*args):
    print(args)
    
print_args(1, 2, 3)
```

    (1, 2, 3)


In this example, we’re no longer passing a list to `my_sum()`. Instead, we’re passing three different positional arguments. **`my_sum()` takes all the parameters that are provided in the input and packs them all into a single iterable object named `args`.**

The magic is that we use the **unpacking operator** (`*`).  The iterable object you’ll get using the unpacking operator `*` is not a `list` but a `tuple`, which is NOT mutable.

## Using the Python kwargs Variable in Function Definitions

`**kwargs` works just like `*args`, but instead of accepting positional arguments it accepts keyword (or **named**) arguments. 

E.g.:


```python
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", 
                  c="Is", d="Great", e="!"))
```

    RealPythonIsGreat!


Like `args`, `kwargs` is just a name that can be changed to whatever you want. Again, what is important here is the use of the **unpacking operator** (`**`).

Note:  If we [iterate over the dictionary](https://realpython.com/iterate-through-dictionary-python/) and want to return its **values**, we must use `.values()`. Otherwise it will iterates over the **keys** of the kwargs dictionary.

## Ordering Arguments in a Function

The correct order for parameters is:

1. Standard arguments
2. `*args` arguments
3. `**kwargs` arguments

E.g.: 


```python
# correct
def my_function(a, b, *args, **kwargs):
    pass
```

## Forwarding Optional or Keyword Arguments

To pass optional or keyword parameters from one function to another, use the argument-unpacking operators `*` and `**` when calling the function you want to forward arguments to.

This also gives you an opportunity to modify the arguments before you pass them along. E.g.:

```python
def foo(x, *args, **kwargs): 
    kwargs['name'] = 'Alice' 
    new_args = args + ('extra', ) 
    bar(x, *new_args, **kwargs)
```

One scenario where this technique is useful is **writing wrapper functions such as decorators**. There you typically also want to accept arbitrary arguments to be passed through to the wrapped function. If we can do it without having to copy and paste the original function’s signature, that might be more maintainable. E.g.:

```python
def trace(func):
    @functools.wraps(func)
    def wrapper_trace(*args, **kwargs):
        print(func.__name__, args, kwargs)
        result = func(*args, **kwargs)
        print(result)

    return wrapper_trace


@trace
def greet(greeting, name):
    return(f"{greeting}, {name}!")
```

```python
>>> greet("Hello", "Ecko")
greet ('Hello', 'Ecko') {}
Hello, Ecko!
```







## Unpacking With the Asterisk Operators: * & **

In short, the unpacking operators are operators that **unpack the values from iterable objects in Python**. 

- The single asterisk operator `*` can be used on any iterable that Python provides
- The double asterisk operator `**` can only be used on dictionaries

### `*`

The `*` operator works on any iterable object.

For example:


```python
my_list = [1, 2, 3]
print(my_list)
```

    [1, 2, 3]


The list is printed, **along with the corresponding brackets and commas**.

Now try to prepend the unpacking operator `*` to the name of the list: 


```python
print(*my_list)
```

    1 2 3

Putting a `*` before an iterable in a function call will *unpack* it and pass its elements as separate positional arguments to the called function.

Here, the * operator tells `print() `to unpack the list first. In this case, the output is no longer the list itself, but rather the content of the list. The difference is: Instead of a list, `print()` has taken three separate arguments as the input.

Another thing should be noticed is that we used the unpacking operator `*` to call a function, instead of in a function definition. In this case, `print()` takes all the items of a list as though they were single arguments.

#### Other convenient uses of the unpacking operator

##### E.g. 1

Split a list into three different parts: The output should show the first value, the last value, and all the values in between. 

With the unpacking operator, we can do this in just one line of code:


```python
my_list = [1, 2, 3, 4, 5, 6]

a, *b, c = my_list

print(a)
print(b)
print(c)
```

    1
    [2, 3, 4, 5]
    6


##### E.g. 2

Merge two lists:


```python
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

merged_list = [*list_1, *list_2]
merged_list
```




    [1, 2, 3, 4, 5, 6]



#### For strings

In Python, strings are iterable objects. So the `*` operators can also be used to unpack a string.

E.g.:


```python
a = [*'HelloWorld']
a
```




    ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']



The previous example seems great, but when you work with these operators it’s important to keep in mind the seventh rule of [*The Zen of Python*](https://www.python.org/dev/peps/pep-0020/) by Tim Peters: *Readability counts*!

Consider the following example:


```python
*a, = 'HelloWorld'
a
```




    ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']



There’s the unpacking operator `*`, followed by a variable, a comma, and an assignment. That’s a lot packed into one line! In fact, this code is no different from the previous example. It just takes the string `HelloWorld` and assigns all the items to the new list `a`, thanks to the unpacking operator `*`.

**The comma after the `a` does the trick. When you use the unpacking operator with variable assignment, Python requires that your resulting variable is either a list or a tuple. With the trailing comma, you have actually defined a tuple with just one named variable `a`.**

<span style="color: Red">While this is a neat trick, many Pythonistas would not consider this code to be very readable. **As such, it’s best to use these kinds of constructions sparingly.**</span>


### `**`

The `**` operator works similarly as `*`, but only for dictionary.


```python
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}

my_merged_dict = {**my_first_dict, **my_second_dict}
my_merged_dict
```


    {'A': 1, 'B': 2, 'C': 3, 'D': 4}

The `**` operator also works for **function argument unpacking**. 

For example:

```python
def print_vector(x, y, z):
    print(f"<{x}, {y}, {z}>")
    
vec_dict = {
    "y": 1,
    "x": 0,
    "z": 2,
}
```

```python
>>> print_vector(**vec_dict)
<0, 1, 2>
```

Because dictionaries are unordered, this matches up dictionary values and function arguments **based on the dictionary keys**: the `x` argument receives the value associated with the `'x'` key in the dictionary.

If you use the single asterisk (`*`) operator to unpack the dictionary, keys would be passed to the function in *random* order instead.