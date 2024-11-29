"""
URL configuration for MealBridge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from MealBridge import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,views.home,name='home'),
    path('login/' ,views.login,name='login'),
    path('signup/' ,views.signup,name='signup'),
    path('logout/' ,views.logoutPage,name='logout'),
    path('contact/' ,views.contact,name='contact'),
    path('about/' ,views.aboutus,name='abt'),
    path('tiffin/' ,views.vd,name='vd'),
    path('tiffin_bennett/' ,views.vdb,name='vdb'),
    path('tiffin_galgotia/' ,views.vdg,name='vdg'),
    path('tiffin_sharda/' ,views.vds,name='vds'),
    path('tiffin_DTU/' ,views.vdd,name='vdd'),
    
    
    
]
