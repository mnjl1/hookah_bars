from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username = 'dmytro',
            email = 'd@email.com',
            password = '11111'
        )
        self.admin_user = User.objects.create_superuser(
            username = 'admin',
            email = 'admin@email.com',
            password = '11111'
        )
    
    def test_create_user(self):
        self.assertEqual(self.user.username, 'dmytro')
        self.assertEqual(self.user.email, 'd@email.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)

    def test_create_superuser(self):
        self.assertEqual(self.admin_user.username, 'admin')
        self.assertEqual(self.admin_user.email, 'admin@email.com')
        self.assertTrue(self.admin_user.is_active)
        self.assertTrue(self.admin_user.is_staff)
        self.assertTrue(self.admin_user.is_superuser)

