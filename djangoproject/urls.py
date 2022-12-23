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
    path('p_introcloud', views.pandas_graph_commit_intro_word_cloud),
    path('pandas_contricloud',
         views.pandas_graph_commit_contributor_word_cloud),
    path('pytorch_issue_wordcloud', views.pytorch_graph_issues_word_cloud),
    path('pandas_issue_wordcloud', views.pandas_graph_issues_word_cloud),
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
    path('pandas_modi_hour', views.pandas_graph_modi_time_of_day),
    # 比较两个仓库的核心和非核心，包括commit数量，设计讨论和文件修改数目三个维度
    path('comp_commit', views.comp_commit_by_week),
    path('comp_design', views.comp_design_by_week),
    path('comp_file', views.comp_file_by_week),
    # 比较两个仓库，包括commit数量，设计讨论和文件修改数目三个维度
    path('comp_commit_b', views.comp_commit_by_week_brief),
    path('comp_design_b', views.comp_design_by_week_brief),
    path('comp_file_b', views.comp_file_by_week_brief),
    # pytorch的design讨论数量，按周）
    path('desi_week', views.graph_design_by_week),
    path('comm_week', views.graph_commit_by_week),
    path('file_week', views.graph_file_by_week),
    # pandas的design讨论数量，按周）
    path('pandas_desi_week', views.pandas_graph_design_by_week),
    path('pandas_comm_week', views.pandas_graph_commit_by_week),
    path('pandas_file_week', views.pandas_graph_file_by_week),
    # 更新仓库
    path('commit_update', views.commit_update_main),
    path('tttt', views.test),
    path('uuuu', views.commit_update_main),
    path('issuedev', views.pytorch_issue_time),
    path('commitdev', views.pytorch_commit_time),
    # 时间变化的star数目
    path('commit_both', views.commit_both),

    path('issue_both', views.issue_both),

    path('pytorch_update_time', views.pytorch_issue_update_time),
    path('pandas_update_time', views.pandas_issue_update_time),
    path('graph_comtrib', views.pytorch_Contrib_graph),
    path('graph_comtrib_pandas', views.pandas_Contrib_graph),
    path('issue_test', views.issue_content),
    path('issue_test1', views.issue_content1),
    path('update_pytorch', views.update_pytorch),
    path('update_pandas', views.update_pandas),
    # 年commit数目
    # path('commit_year', views.commit_year),
]
