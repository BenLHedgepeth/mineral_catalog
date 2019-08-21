

from django.test import TestCase
from django.http import Http404
from django.template.backends.django import Template

class TestGetTemplate(TestCase):

    def setUp(self):
        self.templates = {
                'valid' : 'index.html',
                'invalid' : 'idex.html'
            }

    # def test_load_page_template_success(self):
    #     ''' 
    #     Explains Template class type - 
        
    #     https://docs.djangoproject.com/en/2.2/topics/
    #     templates/#django.template.loader.get_template
    #     '''
    #     template = load_page_template(self.templates['valid'])
    #     self.assertIn('html', self.templates['valid'])
    #     self.assertIsInstance(template, Template)

    # def test_load_page_template_fail(self):
    #     with self.assertRaises(FileNotFoundError):
    #         load_page_template(self.templates['invalid'])
 


# Create your tests here.

# class ViewNotFound(TestCase):
#     '''
#         To verify that a browswer receives a HTTP 404 
#         response when a path cannot be served due to
#         it not matching any url stored in the server.     
#     '''

#     test_data = '/home'

#     def test_view_response_404(self):
#         with self.assertRaises(Http404):
#             self.client.get('/home_page')




