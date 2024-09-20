import math, matplotlib.pyplot as plt


def distance( p1, p2 ):
    x1, y1= p1
    x2, y2= p2
    x, y= x2-x1, y2-y1
    return math.sqrt( x*x + y*y )

class RegressionLinear():

    def __init__(self, data):
        self._cloud= data
        self._slope= 1.0
        self._yIntercept= 0.0

    # Accessors:
    def data(self):
        return self._cloud
    
    def slope(self):
        return self._slope
    
    def yIntercept(self):
        return self._yIntercept

    def parameterNames(self):
        return ["slope", "y-intercept"]
    
    def parameters(self):
        return [self._slope, self._yIntercept]
    
    # Construction:
    def setData(self, data):
        self._cloud= data

    def setParameters(self, slope, yIntercept):
        self._slope= slope
        self._yIntercept= yIntercept

    # Estimation:
    def estimate(self, x):
        return self._yIntercept + (x * self._slope)
    
    def averageError(self):
        error= 0.0
        for x, y in self.data().points() :
            error+= math.fabs( y - self.estimate(x) )
        return error/self.data().size()

    # Solving:
    def parameterEstimation_first(self):
        # Search extrem points
        points= self.data().points()
        pRef1= points[0]
        pRef2= points[-1]
        refDist= distance( pRef1, pRef2 )
        ok= False
        while not ok :
            ok= True
            for p in points :
                if distance( pRef1, p ) > refDist :
                    pRef2= p
                    refDist= distance( pRef1, pRef2 )
                    ok= False
                elif distance( p, pRef2 ) > refDist :
                    pRef1= p
                    refDist= distance( pRef1, pRef2 )
                    ok= False
        # Compute parameters
        x1, y1= pRef1
        x2, y2= pRef2
        self._slope= (y2-y1)/(x2-x1)
        self._yIntercept= y2-(self._slope*x2)
        return self.parameters()

    def testParametersDelta( self, delta ):
        refSlope= self._slope
        refYI= self._yIntercept
        refError= self.averageError()
        # Test on Slope:
        self._slope= refSlope - delta
        if self.averageError() < refError :
            return True
        # second Test:
        self._slope= refSlope + delta
        if self.averageError() < refError :
            return True
        self._slope= refSlope
        # Test on y-intercept:
        self._yIntercept= refYI - delta
        if self.averageError() < refError :
            return True
        # Test:
        self._yIntercept= refYI + delta
        if self.averageError() < refError :
            return True
        # Else
        self._yIntercept= refYI
        return False

    def optimizeParametersDelta( self, delta ):
        change= False
        while self.testParametersDelta(delta) :
            change= True
        return change
    
    # Plot generation:
    def draw( self, file="regression.png" ):
        plt.plot(
            self._cloud.listX(), self._cloud.listY(),
            color='green',
            marker='o', linestyle=' '
        )
        plt.plot(
            [ -10, 110 ], [ self.estimate(-10), self.estimate(110) ],
            color='red'
        )
        plt.savefig( file )
        plt.clf()

