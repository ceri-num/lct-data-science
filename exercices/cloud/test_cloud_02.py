import myCloud as mc

def test_cloud():
    aCloud= mc.Cloud()
    assert( type(aCloud) == mc.Cloud )
    assert( aCloud.size() == 0 )
    assert( aCloud.points() == [] )

    aCloud.append( 3, 8 )
    
    assert( aCloud.size() == 1 )
    assert( aCloud.points() == [(3.0, 8.0)] )
    assert( aCloud.point(0) == (3.0, 8.0) )

    aCloud.append( 11.0, -2.0 )
    aCloud.append( 0.4, 0 )

    assert( aCloud.size() == 3 )
    assert( aCloud.points() == [(3.0, 8.0), (11.0, -2.0), (0.4, 0.0)] )

    aCloud2= mc.Cloud()
    
    aCloud2.intializeAtRandom(100)
    assert( aCloud2.size() == 100 )
    for i in range(100) :
        for j in range(100) :
            assert( i == j or aCloud2.point(i) != aCloud2.point(j) )
    
    aCloud3= mc.Cloud()
    assert( str(aCloud3) == "[](0)" )
    aCloud3.append( 11.0, -2.0 )
    aCloud3.append( 0.4, 0 )
    assert( str(aCloud3) == "[(11.0, -2.0), (0.4, 0.0)](2)" )
    aCloud3.append( 3.0, 8.0 )
    aCloud3.append( 13.0, 0.4 )
    assert( str(aCloud3) == "[(11.0, -2.0), (0.4, 0.0), ...](4)" )

# If the script is the main script interpreted by Python:
# (i.e. it is not imported from another python file...)
if __name__ == "__main__" : 
    # Perform the test...
    print( "test Cloud (02)" )
    test_cloud()
    print( "OK" )
