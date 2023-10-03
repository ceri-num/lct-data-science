from classif.classifier import Classifier
from classif.classifierCircle import ClassifierCircle
import numpy

def test_classifier_parameter():
    Cls= Classifier()

    assert( Cls.parameterSize() == 1 )
    
    Cls.setParameter( 0, 10,0)
    assert( round( Cls.getParameter(0), 8) == 10.0 )

    # estimate should return the appropriate class-id for a given observation:
    assert( Cls.estimate( [22.8, 6.7] ) == 1 )
    assert( Cls.estimate( [4.7, 12.6] ) == 2 )

def test_classifier_optimization():
    Cls= Classifier()

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

    assert( Cls.countErrors( data1, 1 ) == 0 )
    assert( Cls.countErrors( data2, 2 ) == 0 )

    assert( 2.40 < Cls.getParameter(0) and Cls.getParameter(0) < 8.02 )


def test_classifier_ClassifierCircle():
    Cls= ClassifierCircle()
    
    assert( Cls.parameterSize() == 3 )

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

    assert( Cls.countErrors( data1, 1 ) == 0 )
    assert( Cls.countErrors( data2, 2 ) == 0 )
