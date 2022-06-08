"""kino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app import views;
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.home),
    path('create/',views.createData),
    path('welcometemp/',views.welcome),
    path('projections/',views.projections,name='projections'),
    path('login/',LoginView.as_view(template_name='login.html'), name='login'),
    path('register/',views.register,name = 'register'),
    path('logout/',views.logoutView,name='logout'),
    path('projections/create/',views.createProjection,name='create'),
    path('projections/update/',views.updateProjection,name='update'),
    path('projections/delete/',views.deleteProjection,name='delete'),
    path('obrana/', views.obrana, name='obrana')
    
]
