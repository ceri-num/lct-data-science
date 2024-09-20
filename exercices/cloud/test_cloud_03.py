import myCloud as mc

def test_cloud():
    aCloud= mc.Cloud()
    
    aCloud.intializeAtRandom(100)
    assert( aCloud.size() == 100 )
    for i in range(100) :
        for j in range(100) :
            assert( i == j or aCloud.point(i) != aCloud.point(j) )

    plot= aCloud.plot()
    plot.savefig( "img-test-cloud.png" )

# If the script is the main script interpreted by Python:
# (i.e. it is not imported from another python file...)
if __name__ == "__main__" : 
    # Perform the test...
    print( "test Cloud (02)" )
    test_cloud()
    print( "OK" )
