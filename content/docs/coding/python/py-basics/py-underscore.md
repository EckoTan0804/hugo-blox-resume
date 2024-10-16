---
linktitle: Underscores
summary: ''
weight: 15
title: Underscores in Python
date: 2020-05-01
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

## TL;DR

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Pattern</th>
    <th class="tg-0pky">Example</th>
    <th class="tg-0pky">Meaning</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky"><span style="font-weight:bold">Single Leading Underscore</span></td>
    <td class="tg-0pky"><code>_var</code></td>
      <td class="tg-0pky"><li>Naming convention indicating a name is meant for internal use. </li> <li>Generally not enforced by the Python interpreter (except in wildcard imports) and meant as a hint to the programmer only.</li></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:bold">Single Trailing Underscore</span></td>
    <td class="tg-0pky"><code>var_</code></td>
    <td class="tg-0pky">Used by convention to avoid naming conflicts with Python keywords.</td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:bold">Double Leading Underscore</span></td>
    <td class="tg-0pky"><code>__var</code></td>
      <td class="tg-0pky"><li>Triggers name mangling when used in a class context.</li> <li>Enforced by the Python interpreter.</li></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:bold">Double Leading and Trailing Underscore</span></td>
    <td class="tg-0pky"><span style="font-weight:bold"><code>__var__</code></span></td>
      <td class="tg-0pky"><li>Indicates special methods defined by the Python language. </li> <li>Avoid this naming scheme for your own attributes.</li></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:bold">Single Underscore</span></td>
    <td class="tg-0pky"><code>_</code></td>
      <td class="tg-0pky"><li>Sometimes used as a name for temporary or insignificant variables (“don’t care”).</li> <li>Also: The result of the last expression in a Python REPL.</li></td>
  </tr>
</tbody>
</table>

## Single Leading Underscore: `_var`

When it comes to variable and method names, the single underscore prefix has a meaning by *convention* only.

- It is meant as a **hint** to another programmer that a variable or method starting with a single underscore is intended for internal use.
- It does *NOT* affect the behavior of your programs and this isn't enforced by Python.

Example

```python
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        
t = Test()
print(t.foo)
print(t._bar) # we can still access _bar
```

```txt
11
23
```

However, leading underscores do impact how names get imported from modules. If you use a wildcard import (should be avoided!) to import all names from the module, Python will NOT import names with a leading underscore (unless the module defines an `__all__` list that overrides this behavior).

> Wildcard imports should be avoided as they make it unclear which names are present in the namespace. It’s better to stick to regular imports for the sake of clarity.

Example

**my_module.py**

```python
def external_func():
    print("external")

def _internal_func():
    print("internal")
```

```python
from my_module import *

_internal_func()
```

```txt
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-6-3757d8ee357f> in <module>()
----> 1 _internal_func()

NameError: name '_internal_func' is not defined
```

Unlike wildcard imports, regular imports are not affected by the leading single underscore naming convention:

```python
import my_module

my_module._internal_func()
```

```txt
internal
```

## Single Trailing Underscore: `var_`

Sometimes the most fitting name for a variable is already taken by a keyword. Therefore names like `class` or `def` cannot be used as variable names in Python. In this case you can append a single underscore to break the naming conflict.

Example

```python
def make_obj(name, class_):
    pass
```

## Double Leading Underscore: `__var`

> "**dunder**" in python:
>
> Double underscores are often referred to as [“dunders”](https://nedbatchelder.com/blog/200605/dunder.html) in the Python community. The reason is that double underscores appear quite often in Python code and to avoid fatiguing their jaw muscles Pythonistas often shorten “double underscore” to “dunder.”
>
> For example, you’d pronounce `__baz` as “dunder baz”. Likewise `__init__` would be pronounced as “dunder init”. 

A double underscore prefix causes the Python interpreter to rewrite the attribute name in order to avoid naming conflicts in subclasses. This is also called **name mangling** — the interpreter changes the name of the variable in a way that makes it harder to create collisions when the class is extended later.

Example

```python
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 42
```

```python
>>> t = Test() 
>>> dir(t) # show the list with the object's attributes
['_Test__baz', '__class__', '__delattr__', '__dict__',
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bar', 'foo']
```

This gives us a list with the object’s attributes. There're some interesting findings:

- The `self.foo` variable appears unmodified as foo in the attribute list.
- `self._bar` behaves the same way—it shows up on the class as `_bar`.
- However with `self.__baz`, things look a little different. When you search for `__baz` in that list you’ll see that there is no variable with that name.

If you look closely you’ll see there’s an attribute called `_Test__baz` on this object. This is the name mangling that the Python interpreter applies. **It does this to protect the variable from getting overridden in subclasses.**

Let's create another class that extends the `Test` class and attempts to override its existing attributes added in the constructor:

```python
class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'
```

```python
>>> t2 = ExtendedTest() 
>>> t2.foo
'overridden'
>>> t2._bar 
'overridden'
>>> t2.__baz
AttributeError:
"'ExtendedTest' object has no attribute '__baz'"
```

It turns out this object doesn’t even have a `__baz` attribute. Let's check the list of object's attributes:

```python
>>> dir(t2)
['_ExtendedTest__baz', '_Test__baz', '__class__',
'__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bar', 'foo', 'get_vars']
```

`__baz` got turned into `_ExtendedTest__baz` to prevent accidental modification.

```python
>>> t2._ExtendedTest__baz 
'overridden'
```

The original `_Test__baz` is also still around:

```python
>>> t2._Test__baz
42
```

Double underscore name mangling is fully **transparent** to the programmer. Name mangling affects **ALL** names that start with two underscore characters (“dunders”) in a class context. E.g.

```python
class ManglingTest:
    def __init__(self):
        self.__mangled = "hello"

    def get_mangled(self):
        return self.__mangled
    
    def __method(self):
        return 42
    
    def call_it(self):
        return self.__method()
```

```python
>>> ManglingTest().get_mangled() 
'hello'

>>> ManglingTest().__mangled 
AttributeError:
"'ManglingTest' object has no attribute '__mangled'"
```

```python
>>> MangledMethod().call_it()
42

>>> MangledMethod().__method()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-29-3a27f66f344d> in <module>()
----> 1 MangledMethod().__method()
AttributeError: 'MangledMethod' object has no attribute '__method'
```

## Double Leading and Trailing Underscore: `__var__`

- Name mangling is NOT applied if a name *starts and ends* with double underscores.

- Names that have both leading and trailing double underscores are reserved for special use in the language. 
  - This rule covers things like `__init__` for object constructors, or `__call__` to make an object callable. These dunder methods are often referred to as **magic methods**.
  - It’s best to **stay away** from using names that start and end with double underscores (“dunders”) in your own programs to avoid collisions with future changes to the Python language.

## Single Underscore `_`

### Ignoring Values

If you don't want to use specific values while unpacking, just assign that value to underscore(`_`).

```python
# Ignoring a value
a, _, b = (1, 2, 3)
print(f"a={a}, b={b}")
```

```txt
a=1, b=3
```

You can also use `*_` to ignore multiple values. (Only available in Python 3.x)

```python
a, *_, b = (1, 2, 3, 4, 5, 6, 7)
print(f"a={a}, b={b}")
print(*_)
```

```txt
a=1, b=7
2 3 4 5 6
```

### Use in Looping

```python
for _ in range(5):
    print(_)
```

```txt
0
1
2
3
4
```

### Use in Interprerter

`_` is a special variable in most Python REPLs that represents the result of the last expression evaluated by the interpreter.

```python
>>> 20 + 3
23
>>> _
23
```

## Reference

- [The Meaning of Underscores in Python](https://dbader.org/blog/meaning-of-underscores-in-python)
- [Role of Underscore(_) in Python](https://www.datacamp.com/community/tutorials/role-underscore-python)