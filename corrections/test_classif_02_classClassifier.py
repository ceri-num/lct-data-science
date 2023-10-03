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

def test_classifierInit():
    Cls= clf.Classifier()
    assert( type( Cls ) is clf.Classifier )
    assert( Cls.estimate( [2.8, 12.6] ) in [1, 2] )

def test_classifierYParameter():
    Cls= clf.Classifier()
    Cls._y= 10.0
    # estimate should return the appropriate class-id for a given observation:
    assert( Cls.estimate( [22.8, 6.7] ) == 1 )
    assert( Cls.estimate( [4.7, 12.6] ) == 2 )

def test_classifierCountErrors():
    Cls= clf.Classifier()
    Cls._y= 10.0
    
    data1= numpy.array([ [ 0.5774848, 2.40031608],
        [ 2.13613796, 1.4317355 ],
        [ 0.7319633, 1.72079949],
        [ 1.76813505, 0.54848184],
        [ 0.82877602, -1.30137351],
        [ 5.6747202, 1.95019668] ])
    data2= numpy.array([ [ 7.87792843, 12.87443714],
        [12.59826297, 16.23778898],
        [ 3.55026762, 8.01641115],
        [ 6.80852691, 16.11916979],
        [ 4.75575862, 11.5806246 ],
        [ 6.76888848, 8.13755958] ])

    drawClassif( [data1, data2], Cls._y, 'plot_test_classifierCountErrors.png', style= ['bo', 'go'] )

    assert( Cls.countErrors( data1, 1 ) == 0 )
    assert( Cls.countErrors( data2, 2 ) == 2 )
