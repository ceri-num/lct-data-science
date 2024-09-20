---
marp: false
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

#### La vie est un éternel recommencement…

#### **The life is an eternal restarting…**

---
<!-- --------------------------------------------------------------- -->

![bg](../style/bg-toc3.svg)

<br />

- **Classification**
- **Let's play**

---
<!-- --------------------------------------------------------------- -->

## Classification

The capacity to tag an observation with it appropriate descriptors.
For instance, a _country_ given hearth coordinates.

Latitude | Longitude | Elevation | country
---------|-----------|-----------|-----------
49.70    | 4.92      | 200       | France
49.81    | 5.06      | 230       | Belgique
45.78    | 3.09      | 450       | France
42.70    | 0.79      | 980       | Espagne
...      |           |           |   

What about (_43.40_, _3.66_, _176_) ????

---
<!-- --------------------------------------------------------------- -->

## Classification

<br >
<br >

**More formally:**

$$ \text{predict } Y_i \text{ from } X_i \quad or: \quad  Y_i = \mathit{classifier}( X_i ) $$

<br />

*With:* $Y_i$ defined in a **Finit Countable Set** 

$$Y_i \in [Value_1, Value_2, \ldots, Value_N]$$

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

<br />

<div class="line">
<div class="one2">

**Linear classifier**

Is the data on the *left* or *right* 
from a given vector separation ?

> Support Vector Machines

</div>
<div class="one2">

![](./classif.png)

</div>
</div>



---
<!-- --------------------------------------------------------------- -->

![bg](../style/bg-toc3.svg)

<br />

- Classification
- **Let's play**

---
<!-- --------------------------------------------------------------- -->

## Classifier - Generate data

#### generator: A module function returning a $2\times N$ numpy.array

<div class="line">
<div class="one2">

We wan to generate a 2-dimension
data-set around a given position.

_But_ the closest to the center
the more probable. 

Typically it is possible by using **Gaussian** approach:
With [numpy](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html), for instance.

([Normal Distribution on Wikipedia](https://en.wikipedia.org/wiki/Normal_distribution))

</div>
<div class="one2">

![](./center1.png)

</div>

- Generate 2 data-set and plot them in 2 colors

---
<!-- --------------------------------------------------------------- -->

## Classifier - Simple-Y

<br />

- Simple _y_ Classifier is composed by 1 attribute.
    - The _y_ coordinate, modeling a horizontal separation.
    - (class-1 is considered smaller than _y_ and class-2 greater).
<br />
- Classifier efficiency relies directly on the number of misclassification.
Evaluation of a Classifier requires to confront data-set to their expected class-identifier (1 or 2).
<br />
- Plot the horizontal separation and count the errors.

<br />


---
<!-- --------------------------------------------------------------- -->

## Classifier - Simple-Y : Parameter Optimization

<div class="line">
<div class="one2">

- **Optimize $y$ from
a given 2 class data-set**
  - Initialize bounds (_y-min_, _y-max_)
  - Set up an expected precision _$p$_
  - Search the optimal _y*_
  in the range(_y-min_, _y-max_, _p_)


</div>
<div class="one2">

![width:600](./classif-optim.svg)

</div>
</div>

<br />

---
<!-- --------------------------------------------------------------- -->

## Classifier - Circle : 

### A Circle tries to cash the Class-1 data

<div class="line">
<div class="one2">

  - Attibutes (3):
  Circle center coordinates + radius.
  - Class-2 data are data
   outside the circle.

</div>
<div class="one2">

![width:400](./classif-circle.png)

</div>
</div>

---
<!-- --------------------------------------------------------------- -->

## Classifier - Circle : 

### `ClassifierCircle` should implement

<div class="line">
<div class="one2">

  - plot()
  - countError()
  - getParameterLimits()
  - optimizeParameters( precision )

</div>
<div class="one2">

![width:400](./classif-circle.png)

</div>
</div>


---
<!-- --------------------------------------------------------------- -->

## Classification - ClassifierLinear

#### Compute a Linear Classifier


<div class="line">
<div class="one2">

- **Search for the best separation:**

But maybe it is time to use inheritance <br /> to factorize parameter optimization algorithm into a root class

</div> 
<div class="one2">

![](./2center.png)

</div> 
</div> 


Inheritence: on [Wikipedia](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)) and [in python](https://www.w3schools.com/python/python_inheritance.asp)

---
<!-- --------------------------------------------------------------- -->

## Classification - Make Optimization Generic


#### Transform the optimizer developed for Classifier<br />in a more generic version. 

- manipulate a list of parameters with methods like _getParameters_, _setParameters_, ...  rather than directly the parameter name (_y_ in `ClassifierSimpleY`) for the optimization.
- Loop on all parameters in case of Classifier with several parameters.
- Implement the parameter methods for `ClassifierSimpleY` and `ClassifierCircle`.
- Develope a new chlid: `ClassifierLinear`.

<br />
<br />
