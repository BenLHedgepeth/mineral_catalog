import os.path

from django.test import TestCase
from django.http import Http404
from django.urls import reverse
from .data.retrieve_json import pull_json
from .models import Mineral


class TestUrlConfig(TestCase):
    '''
        To verify that a browswer receives a HTTP 404 
        response when a path cannot be served due to
        it not matching any url stored in the server.     
    '''

    def test_view_response_404(self):
        response = self.client.get('home/')
        self.assertEqual(response.status_code, 404)

    def test_view_response_200(self):
    	response = self.client.get('/')
    	self.assertEqual(response.status_code, 200)



class TestDetailPage(TestCase):

    '''
        To verify that a detail page displays only
        
    '''

    fixtures = ['mineral_test_data.json']
    
    @classmethod
    def setUpTestData(cls):
        cls.test_mineral_name = {
            'title_case' : 'Abhurite',
            'lower_case' : 'abhurite'
        }

    def test_mineral_detail(self):

        response = self.client.get(
            reverse('minerals:class', kwargs= {"mineral" : self.test_mineral.name})
        )
        self.assertTemplateUsed(response, 'minerals/detail.html')
        self.assertIsInstance(response.context['mineral'], dict)
        self.assertEqual(len(response.context['mineral']), 8)
        self.assertNotContains(response, 'color')


    def test_mineral_url(self):
        pass


class TestRandomPage(TestCase):


    def test_random_mineral_selected(self):
        pass
        # response = self.client.get(reverse('minerals:random'), follow=True)
        # print(response)
        # self.assertRedirects(response, 'minerals:class')