from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from .models import MyUser

class FormPermission(models.Model):
    """
    Custom permission to allow viewing but not changing anything.
    """
    class Meta:
        permissions = [
            ("view_only", "Can view but not change anything"), 
        ]
# content_type = ContentType.objects.get_for_model(MyUser)

# permission = Permission.objects.create(
#     codename='view_only',
#     name='Can view but not change anything',
#     content_type=content_type,
# ) 
# user = MyUser.objects.get(email='admin@example.com') 

# # Check if the user has the ADMIN role (is_admin=True)
# if user.role == MyUser.ADMIN:
#     # Get the view_only permission
#     view_only_permission = Permission.objects.get(codename='view_only')
#     # Add the view_only permission to the user
#     user.user_permissions.add(view_only_permission)

# user = MyUser.objects.get(email='admin@example.com')
# user.user_permissions.add('view_dashboard')

# from django.contrib.auth.models import Permission

# # Create a new permission for viewing only
# view_only_permission = Permission.objects.create(
#     codename='view_only',
#     name='Can view but not change anything',
# )
# from django.contrib.auth.models import User
# from django.contrib.auth.models import Group

# # Get the user object
# user = User.objects.get(username='username')

# # Add the permission to the user
# user.user_permissions.add(view_only_permission)