from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from decimal import Decimal

class MenuItemsViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.menu_item1 = Menu.objects.create(Title="Item1", Price=9.99, Inventory=20)
        self.menu_item2 = Menu.objects.create(Title="Item2", Price=14.99, Inventory=15)

    def test_get_menu_items(self):
        # Test GET request to the view
        response = self.client.get('/restaurant/menu/') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)


        # Check if the data returned matches the serialized data
        serialized_data = MenuSerializer([self.menu_item1, self.menu_item2], many=True).data
        self.assertEqual(response.data['results'], serialized_data)

    def test_create_menu_item(self):
        # Test POST request to create a new menu item
        data = {'Title': 'New Item', 'Price': 12.99, 'Inventory': 25}
        response = self.client.post('/restaurant/menu/', data)  
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the new menu item is created in the database
        new_menu_item = Menu.objects.get(Title='New Item')
        self.assertEqual(new_menu_item.Price, Decimal('12.99'))
        self.assertEqual(new_menu_item.Inventory, 25)