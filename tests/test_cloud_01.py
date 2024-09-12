import myCloud as mc

def test_cloud_01():
    aCloud= mc.Cloud()
    assert( type(aCloud) == mc.Cloud )

# If the script is the main script interpreted by Python:
# (i.e. it is not imported from another python file...)
if __name__ == "__main__" : 
    # Perform the test...
    print( "test Cloud (01)" )
    test_cloud_01()
    print( "OK" )
