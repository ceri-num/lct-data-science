import numpy, math, random
import matplotlib.pyplot as plt

class Cloud:
    # Initialisation method call by Python constructor.
    def __init__( self, aListOfPoints= [] ):
        listOfX= [ x for x, y in aListOfPoints ]
        listOfY= [ y for x, y in aListOfPoints ]
        self._listX= numpy.array( listOfX )
        self._listY= numpy.array( listOfY )
    
    # Alternative initialization
    def intializeAtRandom( self, numberOfPonts, scale=100.0 ):
        self._listX= [ random.random()*scale for i in range( numberOfPonts ) ]
        self._listY= [ random.random()*scale for i in range( numberOfPonts ) ]

    # Some accessors:
    def size(self):
        return len( self._listX )
    
    def point(self, i):
        x= (float)(self._listX[i]) # I need a cast explicite from numpy floating point to python float
        y= (float)(self._listY[i]) # same
        return (x, y )
    
    def points(self):
        pts= [
            self.point(i)
            for i in range( self.size() )
        ]
        return pts
    
    def listX(self):
        return self._listX
    
    def listY(self):
        return self._listY
    
    # Computed properties:
    def average(self):
        return (
            numpy.average( self._listX ),
            numpy.average( self._listY )
        )

    # Iterative construction:
    def append(self, x, y):
        self._listX= numpy.append( self._listX, x )
        self._listY= numpy.append( self._listY, y )

    # String generation:

    # String generation:
    def __str__(self):
        size= self.size()
        points= self.points()
        if size == 0 :
            return "[](0)"
        if size < 4 :
            s= str( self.point(0) )
            for p in points[1:] :
                s+= ", " + str(p)
            return f"[{s}]({size})"
        
        return f"[{points[0]}, {points[1]}, ...]({size})"

    # Plot generation:
    def plot( self ):
        plt.plot(
            self._listX, self._listY,
            color='green',
            marker='o', linestyle=' '
        )
        return plt