import os.path

from django.test import TestCase
from django.http import Http404
from django.urls import reverse
from .data.retrieve_json import pull_json
from .models import Mineral

# Create your tests here.

# class TestUrlConfig(TestCase):
#     '''
#         To verify that a browswer receives a HTTP 404 
#         response when a path cannot be served due to
#         it not matching any url stored in the server.     
#     '''

#     def test_view_response_404(self):
#         response = self.client.get('home/')
#         self.assertEqual(response.status_code, 404)

#     def test_vew_response_200(self):
#     	response = self.client.get('/')
#     	self.assertEqual(response.status_code, 200)


class TestDetailPage(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        test_mineral_data = pull_json(os.path.abspath('minerals.json'))
        test_abramovite = test_mineral_data[3]

        Mineral.objects.create(**test_abramovite)


    def test_mineral_detail(self):
        response = self.client.get(
            reverse('minerals:class', kwargs= {"mineral" : test_abramovite['name']})
        )
        self.assertTemplateUsed(response, 'minerals/detail.html')
        self.assertIsInstance(response.context, dict)
        self.assertNotContains(response, 'category')

