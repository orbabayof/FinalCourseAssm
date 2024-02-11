from django.test import TestCase
from restaurant.models import Menu

#TestCase class
class MenuTestCase(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(item.get_item(), "IceCream : 80")