import myCloud as mc

def test_cloud():
    aCloud= mc.Cloud()
    assert( type(aCloud) == mc.Cloud )
    assert( aCloud.size() == 0 )
    assert( aCloud.points() == [] )

    aCloud.append( 3, 8 )
    assert( aCloud.size() == 1 )
    assert( aCloud.points() == [(3,8)] )
    assert( aCloud.point(0) == (3,8) )

    aCloud.append( 11, -2 )
    aCloud.append( 0.4, 0 )

    assert( aCloud.size() == 3 )
    assert( aCloud.points() == [(3,8), (11,-2), (0.4,0)] )

# If the script is the main script interpreted by Python:
# (i.e. it is not imported from another python file...)
if __name__ == "__main__" : 
    # Perform the test...
    print( "test Cloud (02)" )
    test_cloud()
    print( "OK" )
