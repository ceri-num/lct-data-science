#!env python3
# Import pyplot package:
import matplotlib.pyplot as plt
import random

s= random.randint(0, 1000)
s= 320
print( f"Seed: {s}" )
random.seed(s)

# Create a plot from a data set:
X= [ random.random()*100 for i in range(10) ]
Y= [ random.random()*100 for i in range(10) ]

plt.plot( X, Y, color='green', marker='o', linestyle=' ')
plt.xlabel( f"Seed: {s}" )

# Generate the plot:
plt.show()
