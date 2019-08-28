# from django.shortcuts import render

from random import choice

from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
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

            return HttpResponse(
                minerals_page.render({'minerals' : stored_minerals})
            )

class MineralPage(View):
    
    def get(self, request, mineral):
        try:
            mineral_page = get_template('minerals/detail.html')
        except TemplateDoesNotExist:
            raise Http404("Wrong")
        else:
            # random_mineral = choice(Mineral.objects.all())
            try:
                chosen_mineral = Mineral.objects.filter(name__contains=mineral).values()[0]
            except Mineral.DoesNotExist:
                raise Http404
            else:
                mineral_attrs = {}
                for key, value in chosen_mineral.items():
                    if key != "id" and value != "":
                        mineral_attrs.update({key : value})
                return HttpResponse(mineral_page.render({
                        'mineral' : mineral_attrs
                        }
                    )
                )
                

class RandomPage(View):

    def get(self, request):

        return HttpResponse(
            reverse(
                "minerals:class", 
                kwargs={'mineral' : "Abernathyite"}
                )
            )