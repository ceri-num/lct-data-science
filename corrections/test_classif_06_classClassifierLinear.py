import classif, classif.classifierLinear as clf
import math, numpy
import matplotlib.pyplot as plt

def drawClassif( datas, a, b, fileNmae, style= ['bo'] ):
    i= 0
    minX= datas[0][0][0]
    maxX= minX
    for data in datas :
        plt.plot( data.T[0], data.T[1], style[i] )
        # Reccord bounds:
        min= numpy.min( data.T[0] )
        if min < minX :
            minX= min
        max= numpy.max( data.T[0] )
        if max > maxX :
            maxX= max
        # Increment style
        i+= 1
        if i == len(style) :
            i=0
    
    plt.plot( [minX-2, maxX+2], [ a*(minX-2)+b, a*(maxX+2)+b], 'r--' )
    plt.savefig(fileNmae)
    plt.clf()

def test_classifierInit():
    Cls= clf.ClassifierLinear()
    assert( type( Cls ) is clf.ClassifierLinear )
    assert( Cls.estimate( [2.8, 12.6] ) in [1, 2] )

def test_classifierParameters():
    Cls= clf.ClassifierLinear()
    Cls.setLine(0.0001, 10.0)

    assert( Cls.parameterSize() == 2 )
    assert( round( Cls.getParameter(0), 8 ) == 0.0001 )
    assert( round( Cls.getParameter(1), 8 ) == 10.0 )

    # Estimate should return the appropriate class-id for a given observation:
    assert( Cls.estimate( [1.0, 2.2] ) == 1 )
    assert( Cls.estimate( [4.7, 16.6] ) == 2 )

def test_classifierCountErrors():
    Cls= clf.ClassifierCircle()
    Cls.setLine(0.0001, 10.0)
    
    data1= numpy.array([ [ 0.5774848, 2.40031608],
        [ 2.13613796, 1.4317355 ],
        [ 0.7319633, 1.72079949],
        [ 1.76813505, 0.54848184],
        [ 0.82877602, -1.30137351],
        [ 5.6747202, 1.95019668] ])
    data2= numpy.array([ [ 1.87792843, 2.87443714],
        [12.59826297, 16.23778898],
        [ 3.55026762, 8.01641115],
        [ 6.80852691, 16.11916979],
        [ 4.75575862, 11.5806246 ],
        [ 6.76888848, 8.13755958] ])

    a, b= Cls.getLine()
    drawClassif( [data1, data2], a, b, 'plot_test_classifierLine_fixed.png', style= ['bo', 'go'] )

    assert( Cls.countErrors( data1, 1 ) == 0 )
    assert( Cls.countErrors( data2, 2 ) == 2 )

    Cls.optimize()

    assert( Cls.countErrors( data1, 1 ) == 0 )
    assert( Cls.countErrors( data2, 2 ) == 0 )
    drawClassif( [data1, data2], a, b, 'plot_test_classifierLine_optimized.png', style= ['bo', 'go'] )
