from django.test import TestCase, Client
from .serializers import MenuItemSerializer
from .models import MenuItem
from django.test import TestCase


class MenuItemModelTest(TestCase):
    def test_add_menuitem(self):
        new_menuitem = MenuItem.objects.create(
            title="Ice-Cream", price=80, inventory=100)
        self.assertEqual(new_menuitem.title, "Ice-Cream")
        self.assertEqual(new_menuitem.price, 80)
        self.assertEqual(new_menuitem.inventory, 100)


class MenuViewTest(TestCase):
    def setUp(self):
        self.menu_item1 = MenuItem.objects.create(
            title="Pizza", price=12.50, inventory=50)
        self.menu_item2 = MenuItem.objects.create(
            title="Salad", price=8.00, inventory=30)
        self.menu_item3 = MenuItem.objects.create(
            title="Burger", price=10.00, inventory=25)
        self.client = Client()

    def test_getall(self):
        response = self.client.get('/api/menu-items/')
        # unauthorized access to check if permissions work
        self.assertEqual(response.status_code, 401)
