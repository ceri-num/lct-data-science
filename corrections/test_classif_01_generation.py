import classif
import math, numpy
import matplotlib.pyplot as plt

def drawData( data, center, fileNmae, style= 'bo' ):
    plt.plot( data.T[0], data.T[1], style )
    plt.plot( [center[0]], [center[1]], 'rx' )
    plt.savefig(fileNmae)  
    plt.clf()

def test_generatorInit():
    data= classif.generator( [10.0, 10.0], 5.5, 200 )
    drawData( data, [10.0, 10.0], "plot_test_generatorInit" )
    assert( type( data ) is numpy.ndarray )
    assert( len( data ) == 200 )
    for observation in data :
        assert( len( observation ) == 2 )
        assert( type(observation[0]) is numpy.float64 )
        assert( type(observation[1]) is numpy.float64 )

def test_generatorRange():
    data= classif.generator( [10.0, 4.0], 4.1, 1000 )
    drawData( data, [10.0, 10.0], "plot_test_generatorRange" )
    center= [
        round( numpy.average( data.T[0] ), 1),
        round( numpy.average( data.T[1] ), 1)
    ]

    # Test if the center is close to the generator center.
    assert( 9.6 < center[0] and center[0] < 10.4 )
    assert( 3.6 < center[1] and center[1] < 4.4 )
    
    count= 0
    for observation in data :
        if( math.dist( list(observation), [10.0, 4.0]) < 10 ):
            count+= 1

    # Test if most of the observation in the scale range of the center (most than 90%).
    assert( count > 1000//90 )
