from django.urls import path
from . import views


name="minerals"
urlpatterns = [
	path('', views.MineralPage.as_view(), name="mineral_listing"),
	# path('mineral/<str:mineral>/')
]