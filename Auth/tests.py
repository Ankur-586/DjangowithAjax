from django.test import SimpleTestCase
from .forms import AddUser
from .models import MyUser
from django.contrib.auth.models import Group

class AddUserFormTest(SimpleTestCase):
    databases = ['default']  # Add 'default' to allow database queries

    def test_valid_form(self):
        form_data = {
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1990-01-01',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'role': '3'  # Assuming '3' corresponds to 'Student'
        }
        form = AddUser(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        form_data = {
            'email': 'invalidemail',
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1990-01-01',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'role': '3'
        }
        form = AddUser(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Enter a Valid Email Address', form.errors['email'])

    def test_existing_email(self):
        # Create a user with the same email as in the form_data
        MyUser.objects.create(
            email='test@example.com',
            first_name='John',
            last_name='Doe',
            date_of_birth='1990-01-01',
            role=3,
            password='testpassword'
        )
        form_data = {
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1990-01-01',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'role': '3'
        }
        form = AddUser(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('User with this Email address already exists', form.errors['email'])

    # Add more test cases as needed
