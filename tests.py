import unittest


from django.test import TestCase
from django.template.backends.django import Template

from helpers import load_page_template

class TestGetTemplate(TestCase):
    pass

    # def setUp(self):
    #     self.templates = {
    #             'valid' : 'index.html',
    #             'invalid' : 'idex.html'
    #         }

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
 




