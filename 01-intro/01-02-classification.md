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

- **Classification**
- **Let's play**

---
<!-- --------------------------------------------------------------- -->

## Classification

The capacity to tag an observation with it appropriate descriptors.

For instance a _country_ given hearth coordinates.

Latitude | Longitude | Elevation | country
---------|-----------|-----------|-----------



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

Fig

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
