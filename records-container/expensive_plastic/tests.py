from .models import Plastic
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class RecordTest(SimpleTestCase): 

    def test_homepage_status(self):
        self.help_status_code("Plastic")
    
    def test_homepage_template(self): 
        self.check_template_used("Plastic", "home.html")

    def help_status_code(self, url_name):
        url = reverse(url_name) 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def check_template_used(self, url_name, template): 
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, template)

class PlasticTests(TestCase): 

    def setUp(self): 
        self.user = get_user_model().objects.create_user(
            username = "test", 
            password = "pass"
        )

        self.plastic = Plastic.objects.create(
            name='Test Album', 
            author=self.user, 
            artists="Test Artist", 
            description="Test Description", 
        )
        
        self.plastic.save()
        self.record = Plastic.objects.get(pk=1)

    def test_model_content(self): 
        self.assertEqual(self.record, self.plastic)

    def test_model_name(self): 
        self.assertEqual(self.record.name, self.plastic.name)

    def test_create_redirect_home(self): 
        response = self.client.post(reverse("Make_Plastic"),{
            "name" : 'Test Album', 
            "author" : self.user, 
            "artists" : "Test Artist", 
            "description" : "Test Description",
        } 
        , follow=True)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed("home.html")
