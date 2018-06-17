# Permissions And Roles

Some roles are predefined in the fixtures. These roles are always present in 
the app. Permission are created for every endpoint and action that endpoint 
has.


### Creating roles

     ./manage.py loaddata roles

This command creates all the necessary roles required for the app     

### Creating permissions

    ./manage.py update_permissions

This command create all the permissons for the endpoints and maps  the
permissons with roles. The mapping of roles and permissions should be defined inside the 
permissons/helpers.py. Like,

    PERMISSION_MAP = {
        "some_role": [
            ('permission-name', 'some-action')
        ]
    }

		
