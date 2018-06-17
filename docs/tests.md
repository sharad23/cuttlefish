#Tests

* Test all the serializers(unit test) , serialization and deserialization test
* Test all the models(unit test) and the functions
* Test all the endpoints(integration test)

###To see the coverage report 
    coverage report -m experiment/models.py
    
###To run the tests
    coverage run ./manage.py test 
    

### Test Serializers
* Test the serializer by inheriting the helpers/test_mixins

### Test Models
* Test all the functions  of the models using mommy_model