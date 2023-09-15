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

- **Main problems: Regression and Classification**
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

## Regression


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

## Linear Regression
<div class="line">
<div class="one2">

**Data set:**
$$\{ y_i, x_{i1},, x_{i2}, \ldots, x_{ip} \}, \quad i \in [1, n]$$

<br />

**Model:**
$$y_i=  \beta_0 + \beta_1 x_{i1} + \ldots + \beta_p x_{ip} + e_i$$

<br />

**In 2 Dimention ($p=1$):**
$$y_i= a x_{i} + b + e_i$$

</div>
<div class="one2">

![](./linear_regression.png)

(Wikipedia)

</div>
</div>


---
<!-- --------------------------------------------------------------- -->

## Classification

The capacity to tag an observation with it appropriate descriptors.
 
For instance _Mister or Miss?_: 

name | height | waist circ. | chest circ. | Foot size | ... | Genre
-----|--------|-------------|-------------|---|--|--
Bob      | 1m80   |    89 |   81 | 44 | ... | M.
Adriana  | 1m85   |    61 |   87 | 36 | ... | Mrs.
Neymar   | 1m75   |    81 | 96.5 | 43 | ... | M.
..       |     |      |  |  | ... |  
..       |     |      |  |  | ... |  
Camille  | 1m74   |    64 |   66 | 42 | ... | ???

---
<!-- --------------------------------------------------------------- -->

## Classification

<br >
<br >
<br >

**More formally:**

$$ \text{predict } Y_i \text{ from } X_i \quad or: \quad  Y_i = \mathit{classifier}( X_i ) $$

<br />

*But:* $Y_i$ defined in a **Finit Countable Set** 

$$Y_i \in [Value_1, Value_2, \ldots, Value_N]$$

<br >
<br >
<br >


---

## Classification

<div class="line">
<div class="one2" >

**In other terms:**
Space Partitioning or Clustering

<br />
<br />

Example of 2D variables into 17 classes: 

</div>
<div class="one2" >

![](./classif2d.png)

</div>
</div>

---
<!-- --------------------------------------------------------------- -->

## Classification

<div class="line">
<div class="one2">

**Linear classifier**

Is the data on the *left* or *right* 
from a given linear separation ?

> Support Vector Machines

</div>
</div>

<div class="line">
<div class="one2">

</div>
<div class="one2">

**Means Clustering**

What is *the closest* mean 
from a given set of means.

> K-Means

</div>
</div>


---
<!-- --------------------------------------------------------------- -->

![bg](../style/bg-toc3.svg)

<br />

- Main problems: Regression and Classification
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

Numerous of useful function ([average](https://numpy.org/doc/stable/reference/generated/numpy.average.html) for instance):

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

- Main problems: Regression and Classification
- Manipulate a Data-Set in Python
- **Let's play**

---
<!-- --------------------------------------------------------------- -->

## Generate and Annalyse Data

- **Linear Regression**
    - Generate 2D points
    - Compute the linear parameters
- **Classification**
    - Generate 2 point-clouds
    - Compute a Linear Classifier

---
<!-- --------------------------------------------------------------- -->

## Linear Regression

#### Generate a 2D point-cloud

<div class="line">
<div class="one2">

- **Generate random points**
in a $100 \times 100$ rectangle

with the `random()` function from the `random` Package for instance.
(on [w3schools](https://www.w3schools.com/python/module_random.asp))

- **Plot the piont-cloud as**

```python
plt.plot( listX, listY, color='green',
            marker='o', linestyle=' ')
```

</div>
<div class="one2">

![](./cloud-simple.png)

</div>
</div>


---
<!-- --------------------------------------------------------------- -->

## Linear Regression

#### Estimate the linear parameters

<div class="line">
<div class="one2">

- **Try a first estimation**

Compute $a$ and $b$ as $y=ax+b$
Based on the 2 more distant points.

- **Plot the line** from $-10$ to $110$
- **Compute the average error**

</div>
<div class="one2">

![](./cloud-regressor1.png)

</div>
</div>

---
<!-- --------------------------------------------------------------- -->

## Linear Regression

#### Generate again a 2D point-cloud

<div class="line">
<div class="one2">

- **Generate random points**
According to a linear model:

Given $a$, $b$ and $e_{max}$

$$ x_i= random[0,\ 100] $$
$$ y_i= ax_i+b+ random[0,\ e_{max}] $$

</div>
<div class="one2">

![](./cloud-linear.png)

</div>
</div>

---
<!-- --------------------------------------------------------------- -->

## Linear Regression


#### Optimize the linear parameters


<div class="line">
<div class="one2">

- **Optimize $a$**

Search a better $a$ at given distance $d$

Try the model with $a+d$ and $a-d$

Keep the one with a min. average error.

Then repeat.

- **Optimize $b$**

When $a$ is fixed, use the process on $b$.

</div>
<div class="one2">

![](./cloud-regressor2.png)


</div>
</div>


---
<!-- --------------------------------------------------------------- -->

## Linear Regression


#### Optimize the linear parameters


<div class="line">
<div class="one2">

- **Repeat**

Previous algorithm provides a solution at $\text{s}$ estimation error.

You can repeat it with $d=d/2$ 

and again until $d < \epsilon$

$\epsilon$ is the desired maximal error on the model parrameters (e.g. $\epsilon=0.0001$)

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

#### Generate again the linear parameters

<br/>

Several implementation mainly based on the [Linear Least Squares](https://en.wikipedia.org/wiki/Linear_least_squares) exists.

- Find a function in a scientific package
- Compare the result with your solution 


<br/>
<br/>
<br/>

---
<!-- --------------------------------------------------------------- -->

## Classification


#### Generate 2 point-clouds

<br />

- This time the generation is based on 2 centers.

Compute the $\{x_i, y_i\}$ from its associate center
at a random distance $d$
in a random direction $\alpha$.

_But_ the closest to the center the more probable. 

for that we want to use a [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution)

- Plot them in 2 colors


---
<!-- --------------------------------------------------------------- -->

## Classification

<br />
<br />


#### Compute a Linear Classifier

<br />

- Search for the best separation line 

Perpendicular to the linear regression 
build over the 2 point-clouds.

<br />
<br />
