from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack

# Create your tests here.

class SnacksTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Khaled",
             email="khaled@test.com", 
             password="kh123"
        )

        self.snack = Snack.objects.create(
            title="milan", 
            purchaser=self.user, 
            description="Student" 
        )
    
    def test_string_representation(self):
        self.assertEqual(str(self.snack), "milan")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "milan")
        self.assertEqual(f"{self.snack.purchaser}", "Khaled")
        self.assertEqual(self.snack.description,"Student")


    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "milan")
        self.assertTemplateUsed(response, "snack_list.html")


    def test_snack_details_view(self):
        response = self.client.get(reverse('snack_detail', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_snack_create_view(self):
        response = self.client.post(reverse("snack_create"),
            {
                "title": "Kaka",
                "description": "love it",
                "purchaser": self.user
            })

     
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Kaka')
        self.assertContains(response, 'love it')
        self.assertContains(response, 'Khaled')


    def test_snack_update_view(self):
        response = self.client.post(reverse('snack_update', args='1'), {
            'title':'valencia' ,
        })
        self.assertContains(response, 'valencia')

    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)