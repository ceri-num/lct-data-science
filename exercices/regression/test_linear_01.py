import time

import myCloud as mc
from regression import RegressionLinear

def test_regression():
    aCloud= mc.Cloud() # Instanciate a new Cloud
    aCloud.intializeAtRandom(50)

    assert( aCloud.size() == 50 )

    reg= RegressionLinear( aCloud )

    assert( type(reg) == RegressionLinear )
    assert( reg.data() == aCloud )
    
    assert( reg.slope() == 1.0 )
    assert( reg.yIntercept() == 0.0 )

    assert( reg.parameterNames() == ["slope", "y-intercept"] )
    assert( reg.parameters()     == [1.0, 0.0] )

    assert( reg.estimate(-10.0) == -10.0 )
    assert( reg.estimate(110.0) == 110.0 )

    reg.draw()
    time.sleep(1)

# If the script is the main script interpreted by Python:
# (i.e. it is not imported from another python file...)
if __name__ == "__main__" : 
    # Perform the test...
    print( "test regression (01)" )
    test_regression()
    print( "OK" )
