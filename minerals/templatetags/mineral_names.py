from django import template
from django.template.defaultfilters import stringfilter
from django.utils.text import slugify


register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def url_slug(name):
	return slugify(name, allow_unicode=True)