# from django.shortcuts import render

from random import choice

from django.views import View
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.urls import reverse
from django.template.loader import get_template

from .models import Mineral


class MineralsPage(View):

    def get(self, request):
        try:
            minerals_page = get_template('minerals/main.html')
        except TemplateDoesNotExist:
            raise Http404("Not here")
        else:
            stored_minerals = Mineral.objects.all()

            return HttpResponse(minerals_page.render({
                    'minerals': stored_minerals,
                    'random': choice(stored_minerals)
                }))


class MineralPage(View):
    def get(self, request, mineral):
        try:
            mineral_page = get_template('minerals/detail.html')
        except TemplateDoesNotExist:
            raise Http404("Wrong")
        else:
            random_mineral = choice(Mineral.objects.all())

            '''
                filter() will not catch Model.DoesNotExist
                exception inside a try block. If there is
                no model instance returned, the result is None.'''
            chosen_mineral = Mineral.objects.filter(
                    name__icontains=mineral).values().first()
            if not chosen_mineral:
                raise Http404
            else:
                mineral_attrs = {}
                for key, value in chosen_mineral.items():
                    if key != "id" and value != "":
                        mineral_attrs.update({key: value})
                return HttpResponse(mineral_page.render({
                    'mineral': mineral_attrs,
                    'random': random_mineral
                    }))
