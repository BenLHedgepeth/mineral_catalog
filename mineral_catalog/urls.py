"""mineral_catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views as main_views
from minerals import views as mineral_views

from django.conf import settings
from django.conf.urls.static import static

minerals_patterns = ([
    path('', mineral_views.MineralsPage.as_view(), name="listing_page"),
    path('<str:mineral>/', mineral_views.MineralPage.as_view(), name="class")
    ], 'minerals'
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(minerals_patterns)),
]
