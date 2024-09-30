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

#### Beautiful Cloud - a 2-Dimension data Structure

<div class="line">
<div class="one2">

We wan to generate Clouds
around a given position.

_But_ the closest to the center
the more probable. 

Typically it is possible by using **Gaussian** approach:
With [numpy](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html), for instance.

([Normal Distribution on Wikipedia](https://en.wikipedia.org/wiki/Normal_distribution))

</div>
<div class="one2">

![](./center1.png)

</div>

---
<!-- --------------------------------------------------------------- -->

## Classifier - Generate data

#### Classifier: A object based on $2$ Clouds.

<div class="line">
<div class="one2">

We wan to generate 2 Clouds
around a given position.


- Generate a 2-clouds data set <br />and plot them in 2 colors

**The second cloud is always the cloud with a greater average $y$ coordinate.**

</div>
<div class="one2">

![](./2-clouds.svg)

</div>

---
<!-- --------------------------------------------------------------- -->


## Classifier - Simple-Y

- Simple _$y$_ Classifier is composed by $1$ attribute.
    - The _$y$_ coordinate, modeling a horizontal separation.
    - class-1 is considered smaller than _$y$_ and class-2 greater.
- Classifier efficiency relies directly on the number of misclassification.
Evaluation of a Classifier requires to confront the data set to their predicted class by the model (1 or 2).
<br />
- To-Do:
  - Initialize a _$y$_ value as you want.
  - Plot the horizontal separation.
  - Count the errors based on a `predictClass(x, y)` method.

<br />


---
<!-- --------------------------------------------------------------- -->

## Classifier - Simple-Y : Parameter Optimization

<div class="line">
<div class="one2">

- **Optimize $y$** considering 2 Clouds:
  - Initialize with an heuristic _$y=y^0$_
  - Search the optimal _$y^*$_ <br /> considering a delta _$d$_ <br />by moving _y_ with _$\pm d$_


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

### `ClassifierCircle` should implement <br />the same methods as `ClassifierSimpleY`

<div class="line">
<div class="one2">

  - initializeParameters()
  - predictClass(x, y)
  - countError()
  - plot()
  - optimizeParameters( precision )
  - ...

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


Inheritance: on [Wikipedia](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)) and [in python](https://www.w3schools.com/python/python_inheritance.asp)

---
<!-- --------------------------------------------------------------- -->

## Classification - Make Optimization Generic


#### Transform the optimizer developed for Classifier<br />in a more generic version. 

- Manipulate a list of parameters with methods like _getParameters_, _setParameters_, ...  rather than directly the parameter name (_y_ in `ClassifierSimpleY`) for the optimization.
- Loop on all parameters in case of Classifier with several parameters.
- Implement the parameter methods for `ClassifierSimpleY` and `ClassifierCircle`.
- Develope a new child: `ClassifierLinear`.
- **Apply a dichotomy-search style:**
  Repeat the optimization process by dividing the delta $d$ by $2$ <br /> until a parameter _$\epsilon$_ value is reached.

<br />
<br />
