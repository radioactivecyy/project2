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
from django.urls import path,include
from django.conf import settings
from django.views import static
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from app import views
from app import contribution
from app import commit

urlpatterns = [
    path('',views.real_index),
    path('admin/', admin.site.urls),
    path('contribution_from',contribution.Contribution_from),
    path('index',views.index),
    path('commit',views.commit),
    path('home',views.real_index),
    path('user',views.user),
    path('real_index',views.real_index),
    path('about_us',views.about_us),
    path('notfound',views.notfound),
    path('intro',views.intro),
    path('commit_from',commit.commit_from),
    path('star_gazer',views.star_gazer),
    path('issue',views.issue),
    path('committer',views.committer),
    path('test_update',views.update),
    path('star1',views.pandas_star_gazer),
    path('issue1',views.pandas_issue),
    path('committer1',views.pandas_committer),
    path('test1',views.pandas_update),
]
