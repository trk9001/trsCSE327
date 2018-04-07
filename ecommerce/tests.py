from django.test import TestCase
from django.test import Client
from .forms import *   # import all forms

# Testing the Registration Form
class Setup_Class(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="user", email="user@mp.com", password="user", password2="user")

class User_RegistrationForm_Test(TestCase):

    # Valid Form Data
    def test_RegisterForm_valid(self):
        form = RegisterForm(data={'username': "user", 'email': "user@mp.com", 'password': "user", 'password2': "user"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_RegisterForm_invalid(self):
        form = RegisterForm(data={'username': "mp", 'email': "", 'password': "mp",'password2': "mp"})
        self.assertFalse(form.is_valid())



# Testing the Login Form
class Setup_Class(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="myuser", password="mypass")
    
class User_LogInForm_Test(TestCase):
    
    # Valid Form Data
    def test_LoginForm_valid(self):
        form = LoginForm(data={'username':"myuser",'password':"mypass"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_LoginForm_invalid(self):
        form = LoginForm(data={'username':"shee",'password':""})
        self.assertFalse(form.is_valid())                              



# Testing the Contact Form
class Setup_Class(TestCase):  
    def setUp(self):
        self.user = User.objects.create(fullname="shakib", email="shakib@gmail.com", content="This is my life.")

class User_ContactForm_Test(TestCase):
    
    # Valid Form Data
    def test_ContactForm_valid(self):
        form = ContactForm(data={'fullname':"shakib",'email':"shakib@gmail.com",'content':"This is my life."})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_ContactForm_invalid(self):
        form = ContactForm(data={'fullname':"",'email':"",'content':""})
        self.assertFalse(form.is_valid())    