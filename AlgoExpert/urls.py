"""AlgoExpert URL Configuration

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

from algorithms.views import home_view, algorithm_detail_view, algorithm_list_view
from feedbacks.views import profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home_view, name="Home"),
    path('', home_view, name="Home"),
    path('algorithms', algorithm_list_view),
    path('algorithms/<int:algorithm_id>', algorithm_detail_view),
    path('profile', profile_view, name="Profile"),
    path('api/feedbacks/', include('feedbacks.urls'))
]
