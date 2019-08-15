from django.template.loader import get_template
from django.template import TemplateDoesNotExist
   
def load_page_template(template_file):
    ''' checks that a template file is saved'''
    try:
        return get_template(template_file)
    except TemplateDoesNotExist:
        raise FileNotFoundError