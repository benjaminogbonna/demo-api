from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from .models import CustomUser

# User Model tests

# class UsersManagersTests(TestCase):
#
#     def test_create_user(self):
#         User = get_user_model()
#         user = User.objects.create_user(username='testuser', email="normal@user.com", password="foo")
#         self.assertEqual(user.email, "normal@user.com")
#         self.assertEqual(user.username, "testuser")
#         self.assertTrue(user.is_active)
#         self.assertFalse(user.is_staff)
#         self.assertFalse(user.is_superuser)
#         with self.assertRaises(TypeError):
#             User.objects.create_user()
#         with self.assertRaises(TypeError):
#             User.objects.create_user(username='', email="")
#         with self.assertRaises(ValueError):
#             User.objects.create_user(username='', email="", password="foo")
#
#     def test_create_superuser(self):
#         User = get_user_model()
#         admin_user = User.objects.create_superuser(username='testuser', email="super@user.com", password="foo")
#         self.assertEqual(admin_user.username, "testuser")
#         self.assertEqual(admin_user.email, "super@user.com")
#         self.assertTrue(admin_user.is_active)
#         self.assertTrue(admin_user.is_staff)
#         self.assertTrue(admin_user.is_superuser)
#         with self.assertRaises(ValueError):
#             User.objects.create_superuser(
#                 username='testuser', email="super@user.com", password="foo", is_superuser=False)

class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user_data = {
            "email": "testuser@example.com",
            "username": "testuser",
            "name": "Test User",
            "phone": "1234567890",
            "address": "123 Test Street",
            "city": "Test City",
            "country": "Test Country",
            "agreed_to_terms_and_p_policy": True,
        }
        self.user = CustomUser.objects.create_user(
            username=self.user_data["username"],
            email=self.user_data["email"],
            password="securepassword",
            agreed_to_terms_and_p_policy=self.user_data["agreed_to_terms_and_p_policy"],
            name=self.user_data["name"],
            phone=self.user_data["phone"],
            address=self.user_data["address"],
            city=self.user_data["city"],
            country=self.user_data["country"],
        )

    def test_user_creation(self):
        """Test that a CustomUser instance is created successfully."""
        self.assertEqual(self.user.email, self.user_data["email"])
        self.assertEqual(self.user.username, self.user_data["username"])
        self.assertTrue(self.user.check_password("securepassword"))
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertTrue(self.user.agreed_to_terms_and_p_policy)

    def test_string_representation(self):
        """Test the string representation of the user."""
        self.assertEqual(str(self.user), self.user_data["username"])

    def test_email_field_uniqueness(self):
        """Test that the email field must be unique."""
        with self.assertRaises(Exception):
            CustomUser.objects.create_user(
                username="duplicateuser",
                email=self.user_data["email"],
                password="securepassword",
                agreed_to_terms_and_p_policy=True,
            )

    def test_username_field_uniqueness(self):
        """Test that the username field must be unique."""
        with self.assertRaises(Exception):
            CustomUser.objects.create_user(
                username=self.user_data["username"],
                email="anotheremail@example.com",
                password="securepassword",
                agreed_to_terms_and_p_policy=True,
            )

    def test_default_values(self):
        """Test that default values are set correctly."""
        user = CustomUser.objects.create_user(
            username="defaultuser",
            email="defaultuser@example.com",
            password="securepassword",
            agreed_to_terms_and_p_policy=True,
        )
        self.assertEqual(user.phone, "")
        self.assertEqual(user.address, "")
        self.assertEqual(user.city, "")
        self.assertEqual(user.country, "")

    def test_user_update(self):
        """Test that user fields can be updated successfully."""
        self.user.name = "Updated Name"
        self.user.save()
        self.assertEqual(self.user.name, "Updated Name")

    def test_required_fields(self):
        """Test that required fields are validated."""
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(
                username=None,
                email="missingusername@example.com",
                password="securepassword",
                agreed_to_terms_and_p_policy=True,
            )

        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(
                username="missingemail",
                email=None,
                password="securepassword",
                agreed_to_terms_and_p_policy=True,
            )

    def test_superuser_creation(self):
        """Test the creation of a superuser."""
        superuser = CustomUser.objects.create_superuser(
            username="adminuser",
            email="admin@example.com",
            password="securepassword",
            agreed_to_terms_and_p_policy=True,
        )
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_agreed_to_terms_validation(self):
        """Test that the agreed_to_terms_and_p_policy field is required."""
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(
                username="noagreement",
                email="noagreement@example.com",
                password="securepassword",
                agreed_to_terms_and_p_policy=False,
            )

# View Tests
class UserAPITestCase(APITestCase):
    def test_user_registration(self):
        data = {
            "email": "test@example.com",
            "username": "testuser",
            "password": "securepassword",
            "agreed_to_terms_and_p_policy": True,
        }
        response = self.client.post("/chat-api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["email"], "test@example.com")
