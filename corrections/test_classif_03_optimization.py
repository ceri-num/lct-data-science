import classif, classif.classifier as clf
import math, numpy
import matplotlib.pyplot as plt

def drawClassif( datas, y, fileNmae, style= ['bo'] ):
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
    
    plt.plot( [minX-2, maxX+2], [y, y], 'r--' )
    plt.savefig(fileNmae)
    plt.clf()

def test_classifier_optimization():
    Cls= clf.Classifier()
    data1= numpy.array([ [ 0.57, 2.40],
        [ 2.13, 1.43 ],
        [ 0.73, 1.72],
        [ 1.76, 0.54],
        [ 0.82, -1.30],
        [ 5.67, 1.95] ])
    data2= numpy.array([ [ 7.87792843, 12.87443714],
        [12.59, 16.23],
        [ 3.55, 8.01],
        [ 6.80, 16.11],
        [ 4.75, 11.58 ],
        [ 6.76, 8.13] ])
    
    Cls.optimize( data1, data2 )
    drawClassif( [data1, data2], Cls._y, 'plot_test_optimization.png', style= ['bo', 'go'] )

    assert( Cls.countErrors( data1, 1 ) == 0 )
    assert( Cls.countErrors( data2, 2 ) == 0 )

    assert( 2.40 < Cls._y and Cls._y < 8.02 )
