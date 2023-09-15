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
