# from django.shortcuts import render



from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.template import TemplateDoesNotExist
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
                minerals_page.render({'minerals' : stored_minerals}, request)
            )

class MineralPage(View):
    
    def get(self, request, mineral):

        try:
            mineral_page = get_template('minerals/detail.html')
        except TemplateDoesNotExist:
            raise Http404("Wrong")
        else:
            try:
                chosen_mineral = Mineral.objects.filter(name__contains=mineral).values()
            except Mineral.DoesNotExist:
                raise Http404
            else:
                mineral_attrs = {}
                print(chosen_mineral)
                # for key, value in chosen_mineral.items():
                #     if value != "":
                #         mineral_attrs[key] = value
                return mineral_page.render({'mineral' : mineral_attrs}, request)

