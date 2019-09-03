import os.path

from django.test import TestCase
from django.http import Http404
from django.urls import reverse
from .data.retrieve_json import pull_json
from .models import Mineral
from .views import MineralPage


class TestUrlConfig(TestCase):
    '''
        To verify that a browswer receives a HTTP 404 
        response when a path cannot be served due to
        it not matching any url stored in the server.     
    '''

    def test_view_response_404(self):
        response = self.client.get('rock/')
        self.assertEqual(response.status_code, 404)

    def test_view_response_200(self):
    	response = self.client.get('/')
    	self.assertEqual(response.status_code, 200)



class TestDetailPage(TestCase):

    '''
        To verify that a detail page displays only
        recorded attributes on record.
    '''

    fixtures = ['mineral_test_data.json']
    
    @classmethod
    def setUpTestData(cls):
        cls.mineral_name = {
            'titlecase' : 'Abhurite',
            'lowercase' : 'abhurite'
        }

    def test_mineral_detail_titlecase(self):

        response = self.client.get(
            reverse('minerals:class', 
                kwargs = {"mineral" : self.mineral_name['titlecase']}
            )
        )
        self.assertTemplateUsed(response, 'minerals/detail.html')
        self.assertIsInstance(response.context['mineral'], dict)
        self.assertEqual(len(response.context['mineral']), 8)
        self.assertNotContains(response, 'color')

    def test_mineral_detail_lowercase(self):
        response = self.client.get(
            reverse('minerals:class', 
                kwargs = {"mineral" : self.mineral_name['lowercase']}
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.app_name, 'minerals')
        self.assertEqual(response.resolver_match.url_name, 'class')

        


