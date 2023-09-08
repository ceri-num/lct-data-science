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

- **One of the main problem: Classification**
- **Manipulate a Data-Set with NumPy**
- **Visualisation with PyPlot**
- **Let's play**

---
<!-- --------------------------------------------------------------- -->

## Data-Science

<br />

"Data science is an interdisciplinary academic field [1] that uses statistics, scientific computing, scientific methods, processes, algorithms and systems to extract or extrapolate knowledge and insights from noisy, structured, and unstructured data." (**[Wikipedia Sept. 2023](https://en.wikipedia.org/wiki/Data_science)**)

<br />

- Higlight Statistics
- Find Causality
- Predict

---
<!-- --------------------------------------------------------------- -->

## Classification

The capacity to tag an observation with it appropriate descriptor.
 
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

Plot exemple.

Simple approximation: _find the hyperplane separation_ (lines in 2D)

---
<!-- --------------------------------------------------------------- -->

![bg](../style/bg-toc3.svg)

<br />

- One of the main problem: Classification
- **Manipulate a Data-Set with NumPy**
- Visualisation with PyPlot
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

Numerus of usefull function ([average](https://numpy.org/doc/stable/reference/generated/numpy.average.html) for instance):

```python
avg = np.average(a)
```

---

## Numpy: Not the only one Science toolkit

<br />
<br />

- [SciPy](https://scipy.org) algorithms for optimization, integration, interpolation, ...
- [Pandas](https://pandas.pydata.org/) a data annalysis lib.
- [Scikit-learn](https://scikit-learn.org) for machine learning
- [PyTorch](https://pytorch.org) dedicated to  deep learning algorithms.
- [opencv-python](opencv.org) focusing on image processing

<br />
<br />
<br />

---
<!-- --------------------------------------------------------------- -->

![bg](../style/bg-toc3.svg)

<br />

- **One of the main problem: Classification**
- **Generate a Data-Set with NumPy**
- **Visualisation with PyPlot**
- **Let's play**

---
<!-- --------------------------------------------------------------- -->


## Point 1


---
<!-- --------------------------------------------------------------- -->

![bg](../style/bg-toc3.svg)

<br />

- **One of the main problem: Classification**
- **Manipulate a Data-Set with NumPy**
- **Visualisation with PyPlot**
- **Let's play**