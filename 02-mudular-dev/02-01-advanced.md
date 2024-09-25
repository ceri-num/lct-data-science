---
marp: true
theme: imt
paginate: true
backgroundImage: url('../style/bg-imt.svg')
---

# Programming (Python) <br /> for Data-Science
### Basics:<br /> Advanced  Programming   

<br />
<br />

**Guillaume.Lozenguez**
[@imt-nord-europe.fr](mailto:guillaume.lozenguez@imt-nord-europe.fr)

![bg](../style/bg-tittle.svg)

---
<!-- --------------------------------------------------------------- -->

![bg](../style/bg-toc3.svg)

<br />

- **Modular Programming**
- **Inheritance and Interface**
- **Good parctices...**
- **Let's play**

---
<!-- --------------------------------------------------------------- -->

## Modular Programming - Definition

<br />

"_Modular Prog._ is a software design technique that emphasizes separating the functionality of a program into independent, interchangeable modules, such that each contains everything necessary to execute only one aspect of the desired functionality." [Wikipedia Sept. 2023](https://en.wikipedia.org/wiki/Modular_programming)

<br />

### In practice:

- Function _>_ Class _>_ **Module**/**Package**/**Namespace**

---
<!-- --------------------------------------------------------------- -->

## Modular Prog. - One file Package (Python)

<div class="line">
<div class="one2">
One file with definitions, instantiations and instructions.

`myPkg.py`
```python
import some.dependencies

def aFunction() :
    ...

class aClass:

aSpecialInstance= aClass()

...
```

</div>
<div class="one2">

then scripts...

`myscript.py`
```python
import myPkg

myPkg.aFunction()
anInstance= myPkg.aClass()
if( anInstance == myPkg.aSpecialInstance )
    ...

```


or 
```python
from myPkg import aFunction
```


</div>

</div>

---
<!-- --------------------------------------------------------------- -->

## Modular Prog. - Python Package

Python modules are not only libraries (ie. a collection of definitions).

**Example with pyplot:**

```python
import matplotlib.pyplot as plt
                                
plt.plot([1, 2, 3, 4])           # Create a plot on an hidden instance of something
plt.ylabel('some numbers')       # feed the hidden instance
plt.savefig('pyplot1.png')     

plt.plot([4, 3, 2, 1])           # Continue to feed the hidden instance
plt.ylabel('some other numbers')
plt.savefig('pyplot2.png')
```

As a result, the `pyplot2.png` includes the 2 graphics.


---
<!-- --------------------------------------------------------------- -->

## Modular Prog. - Python Package

**Example with pyplot:** 

<div class="line">
<div class="one2">

As a result, the `pyplot2.png`
includes the 2 graphics:
(to avoid that: `plt.clf()`)

</div>
<div class="one2">

![](./pyplot.savefig.svg)

</div>
</div>

**On matplotlib (github):**

```python
def savefig(*args, **kwargs) -> None:   
    fig = gcf()                         # get a context, on documentation : 
    res = fig.savefig(*args, **kwargs)  #  | matplotlib.pyplot.gcf()
    fig.canvas.draw_idle()              #  |     Get the current figure.
    return res                          #
```

---
<!-- --------------------------------------------------------------- -->

## Modular Prog. $-$ Complete Packages (Python)

<div class="line">
<div class="one2">

**Tree structure**
of several sub-modules: 

</div>
<div class="one2">

![](./tree-structure.svg)

</div>
</div>
<div class="line">
<div class="one2">

A classical tree view:

<br />

[On Wikipedia](https://en.wikipedia.org/wiki/Tree_structure)

</div>
<div class="one2">

encyclopedia
&ensp;&#9504; culture
&ensp;&#9475; &ensp;&#9504; art
&ensp;&#9475; &ensp;&#9494; craft
&ensp;&#9494; science

</div>
</div>

---
<!-- --------------------------------------------------------------- -->

## Modular Prog. $-$ Complete Packages (Python)

**Tree structure** of python package.  A `__init__.py` in each module directory

_encyclopedia_ example:

<div class="line">
<div class="one2">

**encyclopedia**
&ensp;&#9504; `__init__.py`
&ensp;&#9504; **culture**
&ensp;&#9504; &ensp;&#9504; `__init__.py`
&ensp;&#9475; &ensp;&#9504; `art.py`
&ensp;&#9475; &ensp;&#9494; `craft.py`
&ensp;&#9494; `science.py`

</div>
<div class="one2">

Importing the package modules:

```python
import encyclopedia
# -> load encyclopedia/__init__.py

import encyclopedia.culture
# -> load encyclopedia/culture/__init__.py

import encyclopedia.culture.art
# -> load encyclopedia/culture/art.py

etc...
```

</div>
</div>

---
<!-- --------------------------------------------------------------- -->

## Modular Prog. - Accessing Packages


**Import:** the interpreter _need_ the package location.

- **Inside** your Python script:
The _sys.path_ variable lists the location where resources can be imported

```python
import sys
print( sys.path ) # To notice: `sys.path[0]` matches the script location.
``````

- **Outside** the script, in your shell
An environement variable _PYTHON_PATH_ can be set:

```sh
export PYTHON_PATH="/one/path:/an/other/path" $ echo $PYTHON_PATH
python3 myScript
```

---
<!-- --------------------------------------------------------------- -->

## Modular Prog. - Accessing Packages

- **Realtive** in module trees,
sister-modules can be imported relatively.

<div class="line">
<div class="one2">

**encyclopedia**
&ensp;&#9504; `__init__.py`
&ensp;&#9504; **culture**
&ensp;&#9504; &ensp;&#9504; `__init__.py`
&ensp;&#9475; &ensp;&#9504; `art.py`
&ensp;&#9475; &ensp;&#9494; `craft.py`
&ensp;&#9494; `science.py`

</div>
<div class="one2">

For instance, in `craft.py`

```python
import .art as art
import .. as encyclopedia
import ..science as science

...
```

</div>
</div>


---
<!-- --------------------------------------------------------------- -->

## Modular Prog. - Accessing Packages

<br/>
<br/>

- **Dynamic**
The `importlib` module permits more control in the imports.
For instance, manipulate modules to import as variables.
<br/>
- **Virtualize**
Setup a specific environment for the interpreter.
(Python tools: *venv* - virtual environnement) 

<br/>
<br/>

---
<!-- --------------------------------------------------------------- -->

![bg](../style/bg-toc3.svg)

<br />

- Modular Programming
- **Inheritance and Interface**
- Good parctices...
- Let's play

---
<!-- --------------------------------------------------------------- -->

## Inheritance - An OOP feature

<div class="line">
<div class="one2">

"In object-oriented programming, inheritance is the mechanism of basing an object or class upon another object or class." [Wikipedia, sept. 2023](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))

</div>
<div class="one2">

![](./inheritance.svg)

</div>
</div>

---
<!-- --------------------------------------------------------------- -->

## Inheritance - In python

<div class="line">
<div class="one2">

Parent class:

```python 
class Animal :
    def __init__(self):
        self._attr1= "xxx"
        self._attr2= "yyy"

    def move(self):
        ...
    
    def eat(self):
        ...
```

</div>
<div class="one2">

Child class:

```python 
class Dog(Animal) :          # Inheritance
    def __init__(self):
        super().__init__()   # Parent’s init.
        self._attr3= "zzz"

    def move(self):          # Override
        ...
    
    def bark(self):
        ...
```

</div>
</div>

---
<!-- --------------------------------------------------------------- -->

## Inheritance - In python

**Specificities in python**

- _Overriding_: **Yes**
```python
medor= Dog()
medor.aMethod() # call for Dog:aMethod if exit and Animal:aMethod otherwise
```
- _Access to parent_'s method: `super()` (inside a method)
- _Multiple inheritance_: **Yes** 
```python
class aClass4(aFather, aMother):
   ...
```
- _Abstract Class_: **Not Realy**  (method with `pass` or `assert("to override")`)
    Python modules exit: *abc* (like for enumerate)

---
<!-- --------------------------------------------------------------- -->

## Interface - Another OOP feature

<br />

"In object-oriented programming, an interface or protocol type is a data type that acts as an abstraction of a class." [Wikipedia, sept. 2023](https://en.wikipedia.org/wiki/Interface_(object-oriented_programming))

<div class="line">
<div class="one2">

**Example:**

```
sort(aCollection)
```

Suppose that: 

- _aCollection_ is iterable into _things_
- _things_ can be compared
- _aCollection_ can be re-ordonned

</div>
<div class="one2">

**Langues:**

- C: **Not simple**
- C++: **Template**
- Java: **Interface** 
- Python: **Nativelly**

</div>
</div>

<br />

---
<!-- --------------------------------------------------------------- -->

## Interface - it is natural in Python

<br/>

In python (_Dynamic-Typing Power_), we do not care about the type.
We only care about existing methods.

<br/>

**For instance** 

```python
def best( aThing, anotherThing )
    if aThing.value() >= anotherThing.value() :
        return aThing
    return anotherThing
```

Suppose that _aThing_ and _anotherThing_ both has a method: _value()_.
(potentially: `type(aThing) != type(anotherThing)`)

---
<!-- --------------------------------------------------------------- -->

## Interface - Python built-in interface

Most of the classical operand can be defined, for instance with _addition_:

```python
class ValuableObj:
    def __init__(self, value):
        self._value= value

    def __str__( self ):
        return f"-{self._value}-"
    
    def __add__( self, another ):
        return ValuableObj( self._value + another._value )
    
t1= ValuableObj( 28 )
t2= ValuableObj( 14 ) 

print( t1 + t2 )
```

---
<!-- --------------------------------------------------------------- -->

## Interface - Python built-in interface

- **Comparison:** ( `anInstance == anotherOne` )
`__lt__()`: lesser than, `__le__()`: lesser or equal,
`__gt__()`: greater than, `__ge__()` greater or equal,
`__eq__()`: equal and `__ne__()` not equal
- **Iterable:** ( `for elt in aCollection :` )
`__iter__()`: initialize an iterator. 
and `__next__()`: return the next element of the iteration
(or `raise StopIteration`) 
- **Operation:** $\quad$ `__add__()`, `__sub__()`, `__mul__()`, ...
- **Array:** (`aCollection[i]`) $\quad$ `__getitem__()`

---
<!-- --------------------------------------------------------------- -->

## Exeptions...

<br />
<br />
<br />

To deal with inappropriate events (error)...

[on docs.python.org](https://docs.python.org/fr/3/tutorial/errors.html)


<br />
<br />
<br />
<br />
<br />

---
<!-- --------------------------------------------------------------- -->

![bg](../style/bg-toc3.svg)

<br />

- Modular Programming
- Inheritance and Interface
- **Good practices...**
- Let's play

---
<!-- --------------------------------------------------------------- -->

## Test-Driven Development - Test Comme First

<br />
<br />

"Test-Driven Development (TDD) is a software development process relying on software requirements being converted to __test cases before__ software is fully developed, and tracking all software development by repeatedly testing the software against all test cases. This is as opposed to software being developed first and test cases created later." [Wikipedia sept. 2023](https://en.wikipedia.org/wiki/Test-driven_development)

<br />

_Why?_ - To **test** but also to **well define** the functionality to develop.

<br />

---
<!-- --------------------------------------------------------------- -->

## Test-Driven Development - Test Comme First

#### You wan to develop a functionality<br />Develop the tests of the functionality first.

<div class="line">
<div class="one2">

**1. Specification:**

- need to manipulate points
- compute distance
- set a color
- generate graphics
- ...

**3. Development:**

We know where we go...

</div>
<div class="one2">

**2. Design with a test:**

```python
point1= Point(10.0, 34.5)
point2= Point(12.0, 34.5)

assert(
    round( point1.distance( point2 ), 8 )
    == 2.0
)

point1.setColor( BLUE )

assert( point1.color() == BLUE )

...

```

</div>
</div>

---
<!-- --------------------------------------------------------------- -->

## Test-Driven Development - A Simple Tool: _pytest_

1. **define test cases** in test scripts (all starting by `test_`). 
```python
# test_myFunctionality.py
def test_aFirstTestCase:
    ...
    assert( instruction expected to be True )
    ...

def test_aSecondTestCase:
    ...
```

2. test all your test_case in all your test script (all starting by `test_`).

```sh
# In your favorite shell:
> pip3 install pytest
> python3 -m pytest # or pytest directly
```

---
<!-- --------------------------------------------------------------- -->

## Documents - The 4 mantras

<br />
<br />
<br />

- Clear code
- Comments
- A structured project with an entrance point: the _README_ file
- The documentation...

<br />
<br />
<br />

---
<!-- --------------------------------------------------------------- -->

## Clear code

<br />
<br />
<br />

- Name your variables, function, class and method adequately...
- Small atomic function/methods
- Setup and follow a good practice guide...

#### Python Enhancement Proposals : [pep.python.org](https://peps.python.org/pep-0008/)


<br />
<br />
<br />
<br />

---
<!-- --------------------------------------------------------------- -->

## Comments

```python
def distance(p1, p2):
    # Computes the Euclidean distance between two 2-dimension points. 

    ...

```

or:

```python
def distance(p1, p2):
    '''
    Computes the Euclidean distance between two 2-dimension points. 
    '''

    ...

```


---
<!-- --------------------------------------------------------------- -->

## Structuration & Entrance Point


<div class="line">
<div class="one2">

### Classical directory structuration

**Project directory**
&ensp;&#9504; **docs**
&ensp;&#9504; **src**
&ensp;&#9504; **tests**
&ensp;&#9494; `LICENCE.txt`
&ensp;&#9494; `README.md`
&ensp;&#9494; `pyproject.toml`

</div>
<div class="one2">

### `README.md` the entrance point:

```markdown
# Project Title 

brief description

Meta-data: Authors, Licences, ...

## Installation Instructions


## Get-Started Instructions


## ...
```

</div>
</div>

---
<!-- --------------------------------------------------------------- -->

## Structuration & Entrance point


<div class="line">
<div class="one2">

### Classical directory structuration

**Project directory**
&ensp;&#9504; **docs**
&ensp;&#9504; **src**
&ensp;&#9504; **tests**
&ensp;&#9494; `LICENCE.txt`
&ensp;&#9494; `README.md`
&ensp;&#9494; `pyproject.toml`

</div>
<div class="one2">

### `README.md` in Markdown:

``Markdown is a lightweight markup language for creating formatted text using a plain-text editor'' [wikipedia](https://en.wikipedia.org/wiki/Markdown)


```markdown
# Project Title 

brief description

## Section title

...
```

</div>
</div>

---
<!-- --------------------------------------------------------------- -->

## Structuration - Pip compatible

<div class="line">
<div class="one2">

### Classical directory structuration

**project_directory**
&ensp;&#9504; **docs**
&ensp;&#9504; **src**
&ensp;&#9475; &ensp;&#9494; **myPkg**
&ensp;&#9475; &ensp;&ensp; &ensp;&#9494; \_\_init__.py
&ensp;&#9504; **tests**
&ensp;&#9504; `LICENCE.txt`
&ensp;&#9504; `README.md`
&ensp;&#9494; `pyproject.toml`

then: `> pip install .`

</div>
<div class="one2">

### `pyproject.toml`

Make your project compatible with `pip`

```toml
[build-system]
requires = ["flit_core >= 3.4"]
build-backend = "flit_core.buildapi"

[project]
name = "myPkg"
version = "0.1.0"
authors = [
  { name="Guillaume Lozenguez", email="g.l@imt-ne.fr" },
]
description = "My beautifull package"
readme = "README.md"
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
```

</div>
</div>


---
<!-- --------------------------------------------------------------- -->

## Documents


### Why not in MarkDown ?

**project_directory**
&ensp;&#9504; **docs**
&ensp;&#9504; &ensp;&#9504; index.md
&ensp;&#9504; &ensp;&#9504; aTutorial.md
&ensp;&#9504; &ensp;&#9494; explainations.md
&ensp;&#9504; **src**
&ensp; ...

Then, a tools as `mkdocs` can generate beautifull web/pdf documention... 


---
<!-- --------------------------------------------------------------- -->

![bg](../style/bg-toc3.svg)

<br />

- Modular Programming
- Inheritance and Interface
- Good parctices...
- **Let's play**

---
<!-- --------------------------------------------------------------- -->

## Let's play - Classifier problem

<div class="line">
<div class="one2">

### 1. Decompose into <br />classes and methods

</div>
<div class="one2">

![width:400](./classifiers.svg)

</div>
</div>

---
<!-- --------------------------------------------------------------- -->

## Let's play - Classifier problem

<div class="line">
<div class="one2">

### 2. Derivate the structure of<br />our project directory

</div>
<div class="one2">

![width:400](./classifiers.svg)

</div>
</div>