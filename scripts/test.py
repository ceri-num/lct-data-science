# Definition:
class MyObjectType :
    def method(self) :
        return 42
    
# Use:
anInstance= MyObjectType() # Instanciate a MyObjectType

v1= MyObjectType.method(anInstance)
v2= anInstance.method()

if v1 == v2 :
    print( "Hello World" )
print( f"{MyObjectType.method} \nvs {anInstance.method}")