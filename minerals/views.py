# from django.shortcuts import render



from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.template import TemplateDoesNotExist
from .models import Mineral
from ..helpers import load_page_template

class MineralPage(View):


    def get(self, request):
        try:
            minerals_page = load_page_template('main.html')
        except FileNotFoundError:
            pass
            # return HttpResponseRedirect(reverse('broken'))
        else:
            stored_minerals = Minerals.objects.all()
            return HttpResponse(
                minerals_page.render({'minerals' : select_minerals}, request)
            )

# class MineralPage(View):
#     def get(self, request, mineral):
            
#         try: 
#             selected_mineral = Mineral.objects.get(name__icontains=mineral)
#         except DoesNotExist:
#             pass
#         else:
#             try:
#                 mineral_page = get_template('minerals/mineral.html')
#             except HttpResponseNotFound:
#                 pass
#             else:
#                 return HttpResponse(
#                     mineral_page.render({'mineral' : selected_mineral}, 
#                         request)
#                 )
