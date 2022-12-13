"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.views import static
from django.urls import re_path as url
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_us', views.about_us),
    path('pytorch_star', views.pytorch_star),
    path('star_gazer', views.star_gazer),
    path('issue', views.issue),
    path('pytorch_issue', views.pytorch_issue),
    path('committer', views.committer),
    path('pytorch_committer', views.pytorch_committer),
    path('test_update', views.update),
    path('test1', views.pandas_update),
]
