from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from Auth.manager import MyUserManager

class MyUser(AbstractBaseUser,PermissionsMixin):

    STAFF = 1
    NORMALUSER = 2
    
    ROLE_CHOICES = (
      (STAFF, 'Staff'),
      (NORMALUSER, 'NormalUser'),
    )

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True,null=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    def __str__(self):
        return self.email
    
    @property
    def Full_Name(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        # Check if the user has a specific permission
        if self.is_admin:
            return True  # Superusers have all permissions
        else:
            # Check if the user's role has the required permission
            return self.user_permissions.filter(codename=perm).exists()

    def has_module_perms(self, app_label):
        # Check if the user has permissions to access a specific app/module
        if self.is_admin:
            return True  # Superusers have access to all modules
        else:
            # Check if the user's role has permissions to access the module
            return self.user_permissions.filter(content_type__app_label=app_label).exists()

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin