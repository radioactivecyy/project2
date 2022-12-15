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
    # 词云图
    path('intro_wordcloud', views.graph_commit_intro_word_cloud),
    path('contributor_wordcloud', views.graph_commit_contributor_word_cloud),
    path('pandas_intro_wordcloud', views.pandas_graph_commit_intro_word_cloud),
    path('pandas_contributor_wordcloud', views.pandas_graph_commit_contributor_word_cloud),
    # 复合饼图
    path('compound_pie_commit', views.compound_pie_chart_commit),
    path('compound_pie_design', views.compound_pie_chart_design),
    path('compound_pie_file', views.compound_pie_chart_file),
    # pandas的饼图
    path('pandas_compound_pie_commit', views.pandas_compound_pie_chart_commit),
    path('pandas_compound_pie_design', views.pandas_compound_pie_chart_design),
    path('pandas_compound_pie_file', views.pandas_compound_pie_chart_file),
    # 分时增删行数
    path('modi_hour', views.graph_modi_time_of_day),
    # 比较两个仓库的核心和非核心，包括commit数量，设计讨论和文件修改数目三个维度
    path('comp_commit', views.graph_commit_by_day),
    path('comp_design', views.graph_design_by_day),
    path('comp_file', views.graph_file_by_day),
    # 比较两个仓库的活跃情况
    # 更新仓库
    path('commit_update', views.commit_update_main),
    path('tttt', views.test),
    path('uuuu', views.commit_update_main),
]
