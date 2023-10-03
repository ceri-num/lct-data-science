import classif, classif.classifierCircle as clf
import math, numpy
import matplotlib.pyplot as plt

def drawClassif( datas, center, radius, fileNmae, style= ['bo'] ):
    i= 0
    for data in datas :
        plt.plot( data.T[0], data.T[1], style[i] )
        # Increment style
        i+= 1
        if i == len(style) :
            i=0
    
    plt.gca().add_patch(plt.Circle( center, radius, color='r'))
    plt.savefig(fileNmae)
    plt.clf()

def test_classifierInit():
    Cls= clf.ClassifierCircle()
    assert( type( Cls ) is clf.Classifier )
    assert( Cls.estimate( [2.8, 12.6] ) in [1, 2] )

def test_classifierParameters():
    Cls= clf.ClassifierCircle()
    Cls.setCircle([1.2, 1.8], 2)

    # Estimate should return the appropriate class-id for a given observation:
    assert( Cls.estimate( [1.0, 2.2] ) == 1 )
    assert( Cls.estimate( [4.7, 6.6] ) == 2 )

def test_classifierCountErrors():
    Cls= clf.ClassifierCircle()
    Cls.setCircle([1.2, 1.8], 2)
    
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

    center, radius= Cls.getCircle()
    drawClassif( [data1, data2], center, radius, 'plot_test_classifierCircle.png', style= ['bo', 'go'] )

    assert( Cls.countErrors( data1, 1 ) == 2 )
    assert( Cls.countErrors( data2, 2 ) == 1 )
