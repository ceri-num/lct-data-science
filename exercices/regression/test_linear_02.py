import time, matplotlib.pyplot as plt

import myCloud as mc
from regression import RegressionLinear

def test_regression():
    aCloud= mc.Cloud() # Instanciate a new Cloud
    aCloud.intializeAtRandom(100000)

    assert( aCloud.size() == 100000 )

    reg= RegressionLinear( aCloud )

    print( "> parameters: "+ str( reg.parameterEstimation_first() ))

    if 0.75 < reg.slope() and reg.slope() < 1.15 :
        assert( -1.0 < reg.yIntercept() and reg.yIntercept() < 1.0 )
    elif -0.75 > reg.slope() and reg.slope() > -1.15 :
        assert( 99.0 < reg.yIntercept() and reg.yIntercept() < 101.0 )
    else :
        assert( False )
    
    aveEr= reg.averageError()

    print( "> average error: "+ str( aveEr ))

    assert( 32.5 < aveEr and aveEr < 34.0 )
    
    reg.draw()
    time.sleep(1)

def test_regression_illustration():
    aCloud= mc.Cloud() # Instanciate a new Cloud
    aCloud.intializeAtRandom(1000)

    assert( aCloud.size() == 1000 )

    reg= RegressionLinear( aCloud )
    aveEr= reg.averageError()

    print( "> parameters: "+ str( reg.parameterEstimation_first() ))
    print( "> average error: "+ str( aveEr ))

    assert( 30.0 < aveEr and aveEr < 36.0 )
    
    reg.draw()
    time.sleep(1)


def test_regression_lineCloud():
    aCloud= mc.Cloud() # Instanciate a new Cloud
    aCloud.intializeFromLine( 100, 0.5, -20, 10.0 )

    assert( aCloud.size() == 100 )

    reg= RegressionLinear( aCloud )
    aveEr= reg.averageError()

    print( "> parameters: "+ str( reg.parameterEstimation_first() ))
    print( "> average error: "+ str( aveEr ))

    assert( 0.2 < reg.slope() and reg.slope() < 0.9 )
    assert( -30.0 < reg.yIntercept() and reg.yIntercept() < -10.0 )
    
    plt.plot(
            [ -20, 120 ], [ -20*0.5+-20, 120*0.5+-20 ],
            color='blue'
        )
    reg.draw()
    time.sleep(1)

# If the script is the main script interpreted by Python:
# (i.e. it is not imported from another python file...)
if __name__ == "__main__" : 
    # Perform the test...
    print( "test Cloud (02)" )
    test_regression()
    test_regression_illustration()
    test_regression_lineCloud()
    print( "OK" )
