import myCloud as mc

def test_cloud():
    aCloud= mc.Cloud( [(1.0, 0.0), (0.0, 1.0)] )
    
    listX= [ float(x) for x in aCloud.listX() ]
    listY= [ float(y) for y in aCloud.listY() ]

    assert( listX == [ 1.0, 0.0 ] )
    assert( listY == [ 0.0, 1.0 ] )

    assert( aCloud.average() == (0.5, 0.5) )

    #...

# If the script is the main script interpreted by Python:
# (i.e. it is not imported from another python file...)
if __name__ == "__main__" : 
    # Perform the test...
    print( "test Cloud (02)" )
    test_cloud()
    print( "OK" )
