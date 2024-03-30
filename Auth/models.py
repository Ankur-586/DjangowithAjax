from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from Auth.manager import MyUserManager

class MyUser(AbstractBaseUser, PermissionsMixin):
    ADMIN = 1
    STAFF = 2
    STUDENT = 3
    SUPER_ADMIN = 4  # New super admin role
    
    ROLE_CHOICES = (
      (ADMIN, 'Admin'),
      (STAFF, 'Staff'),
      (STUDENT, 'Student'),
      (SUPER_ADMIN, 'Super Admin'),  # Added new super admin role
    )

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=STUDENT)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)  # Include is_admin here
    is_staff = models.BooleanField(default=False)  # Include is_staff here
    is_superuser = models.BooleanField(default=False)  # Include is_superuser here

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "role"]

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        # Check if the user has a specific permission
        if self.is_superuser:
            return True  # Superusers have all permissions
        else:
            # Check if the user's role has the required permission
            return self.user_permissions.filter(codename=perm).exists()

    def has_module_perms(self, app_label):
        # Check if the user has permissions to access a specific app/module
        if self.is_superuser:
            return True  # Superusers have access to all modules
        else:
            # Check if the user's role has permissions to access the module
            return self.user_permissions.filter(content_type__app_label=app_label).exists()
