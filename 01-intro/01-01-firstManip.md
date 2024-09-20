---
marp: true
theme: imt
paginate: true
backgroundImage: url('../style/bg-imt.svg')
---

# Programming (Python) <br /> for Data-Science
### First Manipulations

<br />
<br />
<br />

**Guillaume.Lozenguez**
[@imt-nord-europe.fr](mailto:guillaume.lozenguez@imt-nord-europe.fr)

![bg](../style/bg-tittle.svg)

---
<!-- --------------------------------------------------------------- -->

![bg](../style/bg-toc3.svg)

<br />

- **A First Problem: Regression**
- **Manipulate a Data-Set in Python**
- **Let's play**

---
<!-- --------------------------------------------------------------- -->

## Data-Science

<br />

"Data science is an interdisciplinary academic field [1] that uses statistics, scientific computing, scientific methods, processes, algorithms and systems to extract or extrapolate knowledge and insights from noisy, structured, and unstructured data." (**[Wikipedia Sept. 2023](https://en.wikipedia.org/wiki/Data_science)**)

<br />

- Highlight Statistics
- Find Causality
- Predict

---
<!-- --------------------------------------------------------------- -->

## A First Problem - Regression

"Regression analysis is a set of statistical processes for estimating the relationships between a dependent variable ($Y_i$) and one or more independent variables ($X_i$)." (**[Wikipedia Sept. 2023](https://en.wikipedia.org/wiki/Regression_analysis)**)

$$ \text{predict } Y_i \text{ from } X_i \quad or: \quad  Y_i = \mathit{regression}( X_i ) $$

**Classically:**

<div class="line">
<div class="one2">

$$ Y_i = f( X_i, \beta ) + e_i \quad \text{with:} $$ 

</div>
<div class="one2">

- $\beta$: the model parameters
(or unknown variables)
- $e_i$: an error

</div>
</div>

*Problem:* Find the best $\beta$ vector minimizing the errors $e_i$


---
<!-- --------------------------------------------------------------- -->

## A First Problem - Linear Regression
<div class="line">
<div class="one2">

**Data set:**
$$\left[ \{ y_i, x_{i1},, x_{i2}, \ldots, x_{ip} \}, \quad i \in [1, n] \right]$$

<br />

**Model:** (a line in a $n$-dimentional space)
$$y_i=  \beta_0 + \beta_1 x_{i1} + \ldots + \beta_p x_{ip} + e_i$$

<br />

**In 2 Dimention ($p=1$):**
$$y_i= a x_{i} + b + e_i$$

</div>
<div class="one2">

![](./linear_regression.png)

([Wikipedia](https://en.wikipedia.org/wiki/Linear_regression))

</div>
</div>


---
<!-- --------------------------------------------------------------- -->

![bg](../style/bg-toc3.svg)

<br />

- A First Problem: Regression
- **Manipulate a Data-Set in Python**
- Let's play

---
<!-- --------------------------------------------------------------- -->

## Numpy: Numerical computing tools

<br />

"NumPy offers comprehensive mathematical functions, random number generators, linear algebra routines, Fourier transforms, and more" <br /> ([numpy.org - sept. 2023](https://numpy.org/))

- On GitHub: 61.1% Python / 36.0% C

<br />

### One of its main feature: 

- Provide a powerful N-dimensional array object

<br />

---
<!-- --------------------------------------------------------------- -->

## Numpy: N-Dimensional Array

Variable Dimention Array:

```python
mySequence = np.array( [1, 2, 3, 4] )
myMatrice = np.array( [[1, 2], [3, 4]] )
my3Dvalues = np.array( [[[1, 2], [3, 4]], [[5, 6], [7, 8]]] )
```

Configurable type:

```python
myTab= np.array([127, 128, 129], dtype=np.int8)
```

Numerous useful function ([average](https://numpy.org/doc/stable/reference/generated/numpy.average.html) for instance):

```python
avg = np.average(a)
```

---

## Numpy: Not the only Science toolkit

<br />
<br />

- [SciPy](https://scipy.org) algorithms for optimization, integration, interpolation, ...
- [Pandas](https://pandas.pydata.org/) a data analysis lib.
- [Scikit-learn](https://scikit-learn.org) for machine learning
- [PyTorch](https://pytorch.org) dedicated to  deep learning algorithms.
- [opencv-python](opencv.org) focusing on image processing

<br />
<br />
<br />

---
<!-- --------------------------------------------------------------- -->

## Data Visualization with Pyplot

"*Matplotlib* is a plotting library for the Python programming language and its numerical mathematics extension *NumPy*." [Wikipedia](https://en.wikipedia.org/wiki/Matplotlib) (and *Pyplot* its API)

![](./pyplot-sample.png)


---
<!-- --------------------------------------------------------------- -->

## Data Visualization with Pyplot

<div class='line'>
<div class='one2'>

```Python
# Import pyplot package:
import numpy
import matplotlib.pyplot as plt

# Create a plot from a data set:
data= numpy.array( [1, 2, 3, 4] )
plt.plot( data )

# Manage graphical design:
plt.ylabel('some numbers')

# Generate the plot:
plt.show()

```

</div>
<div class="one2" >

![](./pyplot.png)

</div>


---

## Data Visualization with Pyplot

<br />
<br />
<br />
<br />
<br />

A huge gallery on : [https://matplotlib.org](https://matplotlib.org/stable/gallery/index.html)

<br />
<br />
<br />
<br />
<br />

---
<!-- --------------------------------------------------------------- -->

![bg](../style/bg-toc3.svg)

<br />

- A First Problem: Regression
- Manipulate a Data-Set in Python
- **Let's play**

---
<!-- --------------------------------------------------------------- -->

## Generate and Annalyse Data

- **Linear Regression**
    - Compute the parameters of a linear regression

---
<!-- --------------------------------------------------------------- -->

## Linear Regression (test 01)

### Setup your working directory:

- Get a fresh start with the [MyCloud Project Correction](https://github.com/ceri-num/lct-data-science/raw/master/corrections/correction-test-cloud.zip)
- Initialize a `RegresionLinear` _class_ into a `regression.py` file.
- Initialize a `test_linear.py` file for testing purpose.


---
<!-- --------------------------------------------------------------- -->

## Linear Regression (test 01)

### Hello-World functionalities

As first functionality, we aims to initiate a `RegresionLinear` over a data-set (i.e a point cloud).

- The class is composed by at least 3 elements:
    * a point cloud (the data)
    * The two parameters of the Regression: <br />$a$ the slope and $b$ the y-intercept. <br />(by default: $a=1$ and $b=0$)

---
<!-- --------------------------------------------------------------- -->

## Linear Regression (test 01)

### Accessors:

As a result, the `RegresionLinear` class defines the methods:

- `data(self):` accessing the point cloud
- `slope(self):` accessing the slope parameter
- `yIntercept(self):` accessing the y-intercept parameter
- `estimate(self, x):` estimating an $y$ given a $x$ ($a\times x+b$)

---
<!-- --------------------------------------------------------------- -->

## Linear Regression (test 01)

### Then visualization:

<div class="line">
<div class="one2">

- A method `draw` generates a _pyplot_ plot: The point cloud,
    The line: $y=ax+b$ <br /> (with $x\in [-10, 110]$)
- At this point, the script `test_linear.py` tests the accessors and draw a random cloud.

</div>
<div class="one2">

![](./regression.png)

</div>
</div>

---
<!-- --------------------------------------------------------------- -->

## Linear Regression (test 01)

### Then visualization:

_Astuce:_ `draw` method should lookalike:

```python
def plot( self, file="regression.png" ):
    plt.plot( the cloud ... )
    plt.plot(  the line a*x+b ... )
    plt.savefig( file )
    plt.clf()
```

This way, the drawing is saved aside <br />rather than in a popped window.

---
<!-- --------------------------------------------------------------- -->

## Linear Regression (test 02)

### First estimation of linear parameters

<div class="line">
<div class="one2">

- **Try a first estimation**

Compute $a$ and $b$ as $y=ax+b$
Based on the 2 more distant points.

**Brute-force algorithm:** 
```
for all combination pi, pj in data
    p1, p2 = max( dist(p1, p2), dist(pi, pj) )
```

</div>
<div class="one2">

![](./cloud-regressor1.png)

</div>
</div>

---
<!-- --------------------------------------------------------------- -->

## Linear Regression (test 02)

### First estimation of linear parameters

<div class="line">
<div class="one2">

- **Compute the average error**

The error $|\widehat{y}_i - y_i|$ between
the observed $y_i$
and it estimation $\widehat{y}_i$ 

$$\widehat{y}_i = ax_i+b$$

- **Tests:** with enough points. <br /> The line is on a diagonal <br /> The average error is close to $33.3$

</div>
<div class="one2">

![](./cloud-regressor1.png)

</div>
</div>

---
<!-- --------------------------------------------------------------- -->

## Linear Regression (test 02)

#### Generate again a 2D point-cloud

<div class="line">
<div class="one2">

- **Generate random points**
According to a linear model:

Given $a$, $b$ and $e_{max}$

$$ x_i= random[0,\ 100] $$
$$ y_i= ax_i+b+ random[-e_{max},\ e_{max}] $$

(Should be associated to `Cloud` class)

- **Test:** First parameter estimation of 
`RegresionLinear` should not be far.

</div>
<div class="one2">

![](./cloud-linear.png)

</div>
</div>

---
<!-- --------------------------------------------------------------- -->

## Linear Regression (test 03)

### Optimize the linear parameters:

Search a better $a$ and $b$ at given delta $d$

Create a method `testParametersDelta` testing:

- _averageError_ with: $(a, \quad b)$
- _averageError_ with: $(a-d, \quad b)$
- _averageError_ with: $(a+d, \quad b)$
- _averageError_ with: $(a, \quad b-d)$
- _averageError_ with: $(a, \quad b+d)$

and keep the best option.

---
<!-- --------------------------------------------------------------- -->

## Linear Regression (test 03)

### Optimize the linear parameters:

Considering that `testParametersDelta` return _True_ if $a$ or $b$ changed

Next method will optimize the parameters at precision $delta$: 

```python
def optimizeParametersDelta( self, delta ):
    change= False
    while self.testParametersDelta(delta) :
        change= True
    return change
```

---
<!-- --------------------------------------------------------------- -->

## Linear Regression (test 04)


### Optimize the linear parameters


<div class="line">
<div class="one2">

- **Repeat Again**

You can repeat it with $delta=delta/2$ 
and again until $delta < \epsilon$

$\epsilon$ is the maximal authorized error
on the model parameters
(e.g. $\epsilon=0.0001$)

$a$ and $b$ are $\epsilon$-optimal

- (test script not provided)
</div>
<div class="one2">

![](./cloud-regressor3.png)

</div>
</div>


---
<!-- --------------------------------------------------------------- -->

## Linear Regression

<br/>
<br/>

### Generate again the linear parameters

<br/>

Several implementation mainly based on the [Linear Least Squares](https://en.wikipedia.org/wiki/Linear_least_squares) exists.

- Find a function in a scientific package
- Compare the result with your solution 


<br/>
<br/>
<br/>

