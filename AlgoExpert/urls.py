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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from algorithms.views import home_view, algorithm_detail_view, algorithm_list_view
from feedbacks.views import profile_view
from django.views.generic import TemplateView

urlpatterns = [
    path('', home_view),
    path('react/', TemplateView.as_view(template_name='react.html')),
    path('api/admin/', admin.site.urls),
    path('api/home', home_view, name="Home"),
    path('api/algorithms', algorithm_list_view),
    path('api/algorithms/<int:algorithm_id>', algorithm_detail_view),
    path('api/profile', profile_view, name="Profile"),
    path('api/feedbacks/', include('feedbacks.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, 
                document_root=settings.STATIC_ROOT)
