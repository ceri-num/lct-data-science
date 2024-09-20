import time, matplotlib.pyplot as plt

import myCloud as mc
from regression import RegressionLinear

def plotRef():
    plt.plot(
            [ -20, 120 ], [ -20*0.5+-20, 120*0.5+-20 ],
            color='blue'
        )

def test_regression():
    aCloud= mc.Cloud() # Instanciate a new Cloud
    aCloud.intializeFromLine( 100, 0.5, -20, 10.0 )

    reg= RegressionLinear( aCloud )
    aveEr= reg.averageError()

    print( "> First parameters:\n\t"+ str( reg.parameterEstimation_first() ))
    print( "> average error:\t"+ str( aveEr ))

    assert( 0.2 < reg.slope() and reg.slope() < 0.9 )
    assert( -30.0 < reg.yIntercept() and reg.yIntercept() < -10.0 )
    
    plotRef()
    reg.draw()
    time.sleep(1)

    oldSlope= reg.slope()
    oldYI= reg.yIntercept()
    if reg.testParametersDelta( 0.1 ) :
        assert( reg.slope() == oldSlope - 0.1
            or reg.slope() == oldSlope + 0.1
            or reg.yIntercept() == oldYI - 0.1
            or reg.yIntercept() == oldYI + 0.1 )
    else :
        assert( reg.slope() == oldSlope and reg.yIntercept() == oldYI )

    aveEr= reg.averageError()

    print( "> One Optim: parameters:\n\t"+ str( reg.parameters() ))
    print( "> average error:\t"+ str( aveEr ))

    reg.setParameters( 0.5, -20 )
    refAveEr= reg.averageError()

    print( "> Init: parameters:\n\t"+ str( reg.parameters() ))
    print( "> average error:\t"+ str( refAveEr ))

    reg.setParameters( oldSlope, oldYI )
    reg.optimizeParametersDelta( 0.1 )
    aveEr= reg.averageError()

    print( "> Optim-0.1 parameters:\n\t"+ str( reg.parameters() ))
    print( "> average error:\t"+ str( aveEr ))

    plotRef()
    reg.draw()
    time.sleep(1)

    reg.optimizeParametersDelta( 0.001 )
    aveEr= reg.averageError()

    print( "> Optim-0.01 parameters:\n\t"+ str( reg.parameters() ))
    print( "> average error:\t"+ str( aveEr ))

    plotRef()
    reg.draw()
    time.sleep(1)

    assert( aveEr <= refAveEr )

# If the script is the main script interpreted by Python:
# (i.e. it is not imported from another python file...)
if __name__ == "__main__" : 
    # Perform the test...
    print( "test Cloud (03)" )
    test_regression()
    print( "OK" )
