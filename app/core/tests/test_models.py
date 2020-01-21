from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """check successfull user creation"""
    def test_create_user_with_email(self):
        email = 'id@gmail.ro'
        password = '1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_valid_email(self):
        '''exception raised if empty username input'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '1234')


    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser('abc@abc.com', '1112')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
