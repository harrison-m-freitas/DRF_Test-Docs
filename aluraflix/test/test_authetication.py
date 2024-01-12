from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class AuthenticationUserTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('programs-list')
        self.user = User.objects.create_user("zoro", password="roronoa")
        
    
    def test_authentication_user(self):
        """Test authentication user"""
        user = authenticate(username="zoro", password="roronoa")
        self.assertTrue((user is not None) and user.is_authenticated)
        
    def test_get_not_authorized(self):
        """Test get request not authorized"""
        response = self.client.get(self.list_url)
        self.assertAlmostEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_failed_user_credentials(self):
        """Test user authentication with wrong credentials"""
        user = authenticate(user="zoro", password="WrongPassword")
        self.assertFalse((user is not None) and user.is_authenticated)
        
        user = authenticate(user="WrongUsername", password="roronoa")
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_get_with_user_autheticated(self):
        """Test get request with user authenticated"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertAlmostEqual(response.status_code, status.HTTP_200_OK)
