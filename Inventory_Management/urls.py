"""
URL configuration for Inventory_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Inventory_models import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('dashboard_page',views.index,name='index'),
    path('alltag',views.alltag,name='alltag'),
    path('config_page',views.config,name='config'),
    path('data',views.data,name='data'),
    path('line_data',views.line_data,name='line_data'),
    path('Tag1',views.Tag1,name='first_tag'),
    path('Tag2',views.Tag2,name='second_tag'),
    path('Tag3',views.Tag3,name='third_tag'),
    path('Tag4',views.Tag4,name='fourth_tag'),
    path('Tag5',views.Tag5,name='fifth_tag'),
    path('Tag6',views.Tag6,name='sixth_tag'),
    path('Tag7',views.Tag7,name='seventh_tag'),
    path('Tag8',views.Tag8,name='eighth_tag'),
    path('cylindrical',views.cylindrical,name='cylindrical'),
    path('conical',views.conical,name='conical'),
    path('conical_data',views.conical_data,name='conical_data'),
    path('cylindrical_data',views.cylindrical_data,name='cylindrical_data'),
    # path('Input',views.Input,name='Input'),

]
