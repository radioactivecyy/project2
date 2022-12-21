import base64
import io
import os
import time

import numpy as np
import numpy.array_api
from PIL import Image
from django.db.models import *
from django.db.models.functions import *
from django.shortcuts import render
from django.views.generic import View
from functools import cmp_to_key
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
import requests
from datetime import datetime

import wordcloud
from matplotlib import pyplot as plt

from .models import stargazer_company, issue_company, \
    stargazer_company_statistic, committer_company_statistic, issue_company_statistic, committer_company, total, \
    pandas_stargazer_company, \
    pandas_issue_company, pandas_committer_company, \
    pandas_total, commit_update, commit_history, commit_by_day, commit_contributors, pandas_commit_by_day, \
    pandas_commit_contributors, pandas_commit_history, pandas_commit_update, pytorch_issues, pandas_issues, \
    pytorch_issues_update_cnt, pandas_issues_update_cnt
import json
from django.http import JsonResponse
from github import Github
import datetime as dt
import github3
import re
import csv

import pandas as pd


def issue_content(request):
    g = Github("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")  # 自己获取的github token
    repo = g.get_repo('pytorch/pytorch')  # 获取pandas项目相关信息
    response = {}
    issues = repo.get_issues()
    print(issues.totalCount)
    i = 0
    for issue in issues:
        i = i + 1
        print(i)
        if i <= 0:
            continue
        else:
            #date = issue.updated_at.strftime("%Y/%m/%d")
            '''if date in response:
                response[date] = response[date] + 1
            else:
                response[date] = 1'''
            if issue.closed_at is None:
                pytorch_issues.objects.create(id=issue.id, created_at=issue.created_at, updated_at=issue.updated_at,
                                              comment_cnt=issue.comments, title=issue.title)
            else:
                pytorch_issues.objects.create(id=issue.id, created_at=issue.created_at, updated_at=issue.updated_at,
                                              closed_at=issue.closed_at,
                                              comment_cnt=issue.comments, title=issue.title)
    '''for key in response:
        pytorch_issues_update_cnt.objects.create(update_date=key, cnt=response[key])'''
    return JsonResponse(response)


def issue_content1(request):
    g = Github("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")  # 自己获取的github token
    repo = g.get_repo('pandas-dev/pandas')  # 获取pandas项目相关信息
    issues = repo.get_issues()
    response = {}
    print(issues.totalCount)
    i = 0
    for issue in issues:
        i = i + 1
        print(i)
        if i <= 0:
            continue
        else:
            #date = issue.updated_at.strftime("%Y/%m/%d")
            '''if date in response:
                response[date] = response[date] + 1
            else:
                response[date] = 1'''
            if issue.closed_at is None:
                pandas_issues.objects.create(id=issue.id, created_at=issue.created_at, updated_at=issue.updated_at,
                                             comment_cnt=issue.comments, title=issue.title)
            else:
                pandas_issues.objects.create(id=issue.id, created_at=issue.created_at, updated_at=issue.updated_at,
                                             closed_at=issue.closed_at,
                                             comment_cnt=issue.comments, title=issue.title)
    '''for key in response:
        pandas_issues_update_cnt.objects.create(update_date=key, cnt=response[key])'''
    return JsonResponse(response)


def pytorch_issue_update_time(request):
    df = pd.read_csv('data/pytorch_issues_update_cnt.csv')
    x = df['update_date'].tolist()
    x = x[::7]
    y = df['cnt'].tolist()
    y = y[::7]
    return JsonResponse({'x': x, 'y': y})

def pandas_issue_update_time(request):
    df = pd.read_csv('data/pandas_issues_update_cnt.csv')
    x = df['update_date'].tolist()
    x = x[::7]
    y = df['cnt'].tolist()
    y = y[::7]
    return JsonResponse({'x': x, 'y': y})


# Create your views here.
def pytorch_issue_time(request):
    # 读文件csv
    df = pd.read_csv('data/issues_pytorch.csv')
    # 读第一列
    x = df['time'].tolist()
    # 七天一个点
    x = x[::7]
    # 读第二列
    y = df['issues'].tolist()
    # 七天一个点
    y = y[::7]
    return JsonResponse({'x': x, 'y': y})


def pytorch_commit_time(request):
    df = pd.read_csv('data/commits_pytorch.csv')
    x = df['time'].tolist()
    x = x[::7]
    y = df['commits'].tolist()
    y = y[::7]
    return JsonResponse({'x': x, 'y': y})


def star_both(request):
    x = [0]
    y = [0]
    # # 读文件csv
    # df = pd.read_csv('data/star_both.csv')
    # # 读第一列
    # x = df['time'].tolist()
    # # 七天一个点
    # x = x[::7]
    # # 读第二列
    # y = df['star'].tolist()
    # # 七天一个点
    # y = y[::7]
    return JsonResponse({'x': x, 'y': y})


def issue_both(request):
    # 读文件csv
    df = pd.read_csv('data/issues_pytorch.csv')
    # 读第一列
    x = df['time'].tolist()
    # 七天一个点

    # 读第二列
    y = df['issues'].tolist()
    # 七天一个点
    df1 = pd.read_csv('data/issues_pandas.csv')
    x1 = df1['time'].tolist()

    y1 = df1['issues'].tolist()
    # 将两个列表合并
    # 填充短的列表
    if len(x) > len(x1):
        x1 = x
    else:
        x = x1
    # 填充y值
    if len(y) > len(y1):
        # 在y1的开头插入len(y)-len(y1)个0
        for i in range(len(y) - len(y1)):
            y1.insert(0, 0)

    else:
        for i in range(len(y1) - len(y)):
            y.insert(0, 0)
    x = x[::7]
    y = y[::7]
    y1 = y1[::7]
    return JsonResponse({'x': x, 'pytorch': y, 'pandas': y1})


def commit_both(request):
    df = pd.read_csv('data/commits_pytorch.csv')
    # 读第一列
    x = df['time'].tolist()
    # 七天一个点

    # 读第二列
    y = df['commits'].tolist()
    # 七天一个点
    df1 = pd.read_csv('data/commits_pandas.csv')
    x1 = df1['time'].tolist()

    y1 = df1['commits'].tolist()
    # 将两个列表合并
    # 填充短的列表
    if len(x) > len(x1):
        x1 = x
    else:
        x = x1
    # 填充y值
    if len(y) > len(y1):
        # 在y1的开头插入len(y)-len(y1)个0
        for i in range(len(y) - len(y1)):
            y1.insert(0, 0)

    else:
        for i in range(len(y1) - len(y)):
            y.insert(0, 0)
    x = x[::7]
    y = y[::7]
    y1 = y1[::7]
    return JsonResponse({'x': x, 'pytorch': y, 'pandas': y1})

def test_connect(request):
    print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
    response = {}
    response['status'] = 1
    return JsonResponse(response)


# Create your views here.
def company_handle(info):
    name = re.sub('[\W_]+', '', info).upper()
    return name


def star_gazer(request):
    # -------------------------------获取数据
    '''g = Github("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")  # 自己获取的github token
    repo = g.get_repo('pytorch/pytorch')  # 获取pytorch项目相关信息
    starcount = repo.stargazers_count
    print(starcount)
    stargazers1 = repo.get_stargazers().reversed
    now_time = dt.datetime.now().strftime('%F %T')
    i = 0
    for people in stargazers1:
        i = i + 1
        print(i)
        if i>starcount-39990: break
        if i <= 0:
            continue
        else:
            if people.company:
                print(company_handle(people.company))
                stargazer_company.objects.create(node_id=people.node_id, company=company_handle(people.company), get_time=now_time)'''
    # --------------------------------------------------------------
    context = HttpResponse(content_type='text/csv')  # 告诉浏览器是text/csv格式
    # csv文件名，不影响
    context['Content-Disposition'] = 'attachment; filename="stargazer_company_statistic.csv"'
    writer = csv.writer(context)
    writer.writerow(['company', 'count', 'total',
                     'update_time', 'duplicate', 'flag'])

    res = []
    for info in stargazer_company_statistic.objects.all():
        res.append([info.company, info.count, info.total,
                    info.update_time, info.duplicate, info.flag])
    # 对res中的数据进行排序
    for i in range(len(res)):
        for j in range(len(res) - 1):
            if res[j][1] < res[j + 1][1]:
                res[j], res[j + 1] = res[j + 1], res[j]
    for info in res:
        writer.writerow(info)
    return context


def pytorch_star(request):
    context = HttpResponse(content_type='text/csv')  # 告诉浏览器是text/csv格式
    # csv文件名，不影响
    context['Content-Disposition'] = 'attachment; filename="stargazer_company_statistic.csv"'
    writer = csv.writer(context)
    writer.writerow(['company', 'count', 'total',
                     'update_time', 'duplicate', 'flag'])
    res = []
    for info in stargazer_company_statistic.objects.all():
        if info.flag == 0:
            # isPytorch
            res.append([info.company, info.count, info.total,
                        info.update_time, info.duplicate, info.flag])
    # 对res中的数据进行排序
    for i in range(len(res)):
        for j in range(len(res) - 1):
            if res[j][1] < res[j + 1][1]:
                res[j], res[j + 1] = res[j + 1], res[j]
    for info in res:
        writer.writerow(info)
    return context


def issue(request):
    # ------------------------------获取issue的assignee信息（可全部获取）
    '''
    g = Github("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")  # 自己获取的github token
    repo = g.get_repo('pytorch/pytorch')  # 获取pytorch项目相关信息
    issues = repo.get_issues()
    now_time = dt.datetime.now().strftime('%F %T')
    i = 0
    for issue in issues:
        i = i + 1
        print(i)
        if i <= 10410:
            continue
        else:
            if issue.assignee is None:
                a=1
            else:
                if issue.assignee.company:
                    print(company_handle(issue.assignee.company))
                    issue_company.objects.create(node_id=issue.assignee.node_id, company=company_handle(issue.assignee.company),
                                                     get_time=now_time)'''
    # -----------------------------------------------------------------------------
    context = HttpResponse(content_type='text/csv')  # 告诉浏览器是text/csv格式
    # csv文件名，不影响
    context['Content-Disposition'] = 'attachment; filename="issue_company_statistic.csv"'
    writer = csv.writer(context)
    writer.writerow(['company', 'count', 'total',
                     'update_time', 'duplicate', 'flag'])
    res = []
    for info in issue_company_statistic.objects.all():
        res.append([info.company, info.count, info.total,
                    info.update_time, info.duplicate, info.flag])
    # 对res中的数据进行排序
    for i in range(len(res)):
        for j in range(len(res) - 1):
            if res[j][1] < res[j + 1][1]:
                res[j], res[j + 1] = res[j + 1], res[j]
    for info in res:
        writer.writerow(info)
    return context


def pytorch_issue(request):
    context = HttpResponse(content_type='text/csv')  # 告诉浏览器是text/csv格式
    # csv文件名，不影响
    context['Content-Disposition'] = 'attachment; filename="issue_company_statistic.csv"'
    writer = csv.writer(context)
    writer.writerow(['company', 'count', 'total',
                     'update_time', 'duplicate', 'flag'])
    res = []
    for info in issue_company_statistic.objects.all():
        if info.flag == 0:
            # isPytorch
            res.append([info.company, info.count, info.total,
                        info.update_time, info.duplicate, info.flag])
    # 对res中的数据进行排序
    for i in range(len(res)):
        for j in range(len(res) - 1):
            if res[j][1] < res[j + 1][1]:
                res[j], res[j + 1] = res[j + 1], res[j]
    for info in res:
        writer.writerow(info)
    return context


def committer(request):
    # ---------------------------------全部获取53127条记录并筛出有公司的记录
    '''g = Github("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")  # 自己获取的github token
    repo = g.get_repo('pytorch/pytorch')  # 获取pytorch项目相关信息
    commits = repo.get_commits().reversed
    print(type(commits))
    now_time = dt.datetime.now().strftime('%F %T')
    i = 0
    print(commits.totalCount)
    for commit in commits:
        i = i + 1
        print(i)
        if i >= 6002:
            break
        if i<=5161:
            continue
        else:
            if commit.author is None:
                a = 1
            else:
                if commit.author.company:
                    print(company_handle(commit.author.company))
                    committer_company.objects.create(node_id=commit.author.node_id,
                                                 company=company_handle(commit.author.company),
                                                 get_time=now_time)'''
    # ------------------------------------------------------------------------
    context = HttpResponse(content_type='text/csv')  # 告诉浏览器是text/csv格式
    # csv文件名，不影响
    context['Content-Disposition'] = 'attachment; filename="committer_company_statistic.csv"'
    writer = csv.writer(context)
    writer.writerow(['company', 'count', 'total',
                     'update_time', 'duplicate', 'flag'])
    # 把数据从数据库中读出来
    # 按照count排序
    res = []
    for info in committer_company_statistic.objects.all():
        res.append([info.company, info.count, info.total,
                    info.update_time, info.duplicate, info.flag])
    # 对res中的数据进行排序
    for i in range(len(res)):
        for j in range(len(res) - 1):
            if res[j][1] < res[j + 1][1]:
                res[j], res[j + 1] = res[j + 1], res[j]
    for info in res:
        writer.writerow(info)
    return context


def pytorch_committer(request):
    context = HttpResponse(content_type='text/csv')  # 告诉浏览器是text/csv格式
    # csv文件名，不影响
    context['Content-Disposition'] = 'attachment; filename="committer_company_statistic.csv"'
    writer = csv.writer(context)
    writer.writerow(['company', 'count', 'total',
                     'update_time', 'duplicate', 'flag'])
    res = []
    for info in committer_company_statistic.objects.all():
        if info.flag == 0:
            # isPytorch
            res.append([info.company, info.count, info.total,
                        info.update_time, info.duplicate, info.flag])
    # 对res中的数据进行排序
    for i in range(len(res)):
        for j in range(len(res) - 1):
            if res[j][1] < res[j + 1][1]:
                res[j], res[j + 1] = res[j + 1], res[j]
    for info in res:
        writer.writerow(info)
    return context


def update(request):
    response = {}
    g = Github("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")  # 填入自己获取的github token
    repo = g.get_repo('pytorch/pytorch')  # 获取pytorch项目相关信息
    now_time = dt.datetime.now().strftime('%F %T')
    # -------------------------------------------更新star_gazer的company信息
    '''stargazer_formal = total.objects.get(source="stargazer").total
    stargazer_now = repo.stargazers_count
    stargazers1 = repo.get_stargazers().reversed
    i = 0
    count = 0
    microsoft_star = 0
    google_star = 0
    facebook_star = 0
    alibaba_star = 0
    bytedance_star = 0
    tencent_star = 0
    thu_star = 0
    pku_star = 0
    baidu_star = 0
    nvidia_star = 0
    zju_star = 0
    for people in stargazers1:
        i = i + 1
        print(i)
        if i > stargazer_now - stargazer_formal: break
        if people.company:
            print(company_handle(people.company))
            count = count + 1
            if "MICROSOFT" in company_handle(people.company):
                microsoft_star = microsoft_star + 1
            if "GOOGLE" in company_handle(people.company):
                google_star = google_star + 1
            if "FACEBOOK" in company_handle(people.company):
                facebook_star = facebook_star + 1
            if "ALIBABA" in company_handle(people.company):
                alibaba_star = alibaba_star + 1
            if "BYTEDANCE" in company_handle(people.company):
                bytedance_star = bytedance_star + 1
            if "TENCENT" in company_handle(people.company):
                tencent_star = tencent_star + 1
            if "TSINGHUAUNIVERSITY" in company_handle(people.company):
                thu_star = thu_star + 1
            if "PEKINGUNIVERSITY" in company_handle(people.company):
                pku_star = pku_star + 1
            if "BAIDU" in company_handle(people.company):
                baidu_star = baidu_star + 1
            if "NVIDIA" in company_handle(people.company):
                nvidia_star = nvidia_star + 1
            if "ZHEJIANGUNIVERSITY" in company_handle(people.company):
                zju_star = zju_star + 1
            stargazer_company.objects.create(node_id=people.node_id, company=company_handle(people.company),
                                             get_time=now_time)
    formal_total = stargazer_company_statistic.objects.get(company="Microsoft",flag=0).total
    formal_total = count + formal_total
    formal = stargazer_company_statistic.objects.get(company="Microsoft",flag=0).count
    stargazer_company_statistic.objects.filter(company="Microsoft",flag=0).update(count=formal + microsoft_star,
                                                                           total=formal_total, update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="Google",flag=0).count
    stargazer_company_statistic.objects.filter(company="Google",flag=0).update(count=formal + google_star, total=formal_total,
                                                                        update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="Facebook",flag=0).count
    stargazer_company_statistic.objects.filter(company="Facebook",flag=0).update(count=formal + facebook_star,
                                                                          total=formal_total, update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="Alibaba",flag=0).count
    stargazer_company_statistic.objects.filter(company="Alibaba",flag=0).update(count=formal + alibaba_star,
                                                                         total=formal_total, update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="ByteDance",flag=0).count
    stargazer_company_statistic.objects.filter(company="ByteDance",flag=0).update(count=formal + bytedance_star,
                                                                           total=formal_total, update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="Tencent",flag=0).count
    stargazer_company_statistic.objects.filter(company="Tencent",flag=0).update(count=formal + tencent_star,
                                                                         total=formal_total, update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="TsinghuaUniversity",flag=0).count
    stargazer_company_statistic.objects.filter(company="TsinghuaUniversity",flag=0).update(count=formal + thu_star,
                                                                                    total=formal_total,
                                                                                    update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="PekingUniversity",flag=0).count
    stargazer_company_statistic.objects.filter(company="PekingUniversity",flag=0).update(count=formal + pku_star,
                                                                                  total=formal_total,
                                                                                  update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="Baidu",flag=0).count
    stargazer_company_statistic.objects.filter(company="Baidu",flag=0).update(count=formal + baidu_star,
                                                                       total=formal_total,
                                                                       update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="NVIDIA",flag=0).count
    stargazer_company_statistic.objects.filter(company="NVIDIA",flag=0).update(count=formal + nvidia_star,
                                                                        total=formal_total,
                                                                        update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="ZhejiangUniversity",flag=0).count
    stargazer_company_statistic.objects.filter(company="ZhejiangUniversity",flag=0).update(count=formal + zju_star,
                                                                                    total=formal_total,
                                                                                    update_time=now_time)'''
    # -----------------------------------------------------------------------------------------------------
    # --------------------------------------------------------更新issue的company信息
    issue_formal = total.objects.get(source="issue").total
    issue_now = repo.get_issues().totalCount
    issues = repo.get_issues().reversed
    i = 0
    count = 0
    microsoft_issue = 0
    quansight_issue = 0
    facebook_issue = 0
    pytorch_issue = 0
    meta_issue = 0
    facebookai_issue = 0
    googlellc_issue = 0
    hhinc_issue = 0
    intel_issue = 0
    nvidia_issue = 0
    for issue in issues:
        i = i + 1
        print(i)
        if i > issue_now - issue_formal:
            print("pytorch issue company update finish!")
            break
        if issue.assignee is None:
            a = 1
        else:
            if issue.assignee.company:
                print(company_handle(issue.assignee.company))
                count = count + 1
                if "MICROSOFT" in company_handle(issue.assignee.company):
                    microsoft_issue = microsoft_issue + 1
                if "QUANSIGHT" in company_handle(issue.assignee.company):
                    quansight_issue = quansight_issue + 1
                if "FACEBOOK" in company_handle(issue.assignee.company):
                    facebook_issue = facebook_issue + 1
                if "PYTORCH" in company_handle(issue.assignee.company):
                    pytorch_issue = pytorch_issue + 1
                if "META" in company_handle(issue.assignee.company):
                    meta_issue = meta_issue + 1
                if "FACEBOOKAI" in company_handle(issue.assignee.company):
                    facebookai_issue = facebookai_issue + 1
                if "GOOGLELLC" in company_handle(issue.assignee.company):
                    googlellc_issue = googlellc_issue + 1
                if "HOOFSANDHORNSINC" in company_handle(issue.assignee.company):
                    hhinc_issue = hhinc_issue + 1
                if "INTEL" in company_handle(issue.assignee.company):
                    intel_issue = intel_issue + 1
                if "NVIDIA" in company_handle(issue.assignee.company):
                    nvidia_issue = nvidia_issue + 1
                issue_company.objects.create(node_id=issue.assignee.node_id,
                                             company=company_handle(
                                                 issue.assignee.company),
                                             get_time=now_time)
    formal_total = issue_company_statistic.objects.get(
        company="Microsoft", flag=0).total
    formal_total = count + formal_total
    formal = issue_company_statistic.objects.get(
        company="Microsoft", flag=0).count
    issue_company_statistic.objects.filter(company="Microsoft", flag=0).update(count=formal + microsoft_issue,
                                                                               total=formal_total, update_time=now_time)
    formal = issue_company_statistic.objects.get(
        company="Quansight", flag=0).count
    issue_company_statistic.objects.filter(company="Quansight", flag=0).update(count=formal + quansight_issue,
                                                                               total=formal_total,
                                                                               update_time=now_time)
    formal = issue_company_statistic.objects.get(
        company="Facebook", flag=0).count
    issue_company_statistic.objects.filter(company="Facebook", flag=0).update(count=formal + facebook_issue,
                                                                              total=formal_total, update_time=now_time)
    formal = issue_company_statistic.objects.get(
        company="Pytorch", flag=0).count
    issue_company_statistic.objects.filter(company="Pytorch", flag=0).update(count=formal + pytorch_issue,
                                                                             total=formal_total, update_time=now_time)
    formal = issue_company_statistic.objects.get(company="Meta", flag=0).count
    issue_company_statistic.objects.filter(company="Meta", flag=0).update(count=formal + meta_issue,
                                                                          total=formal_total, update_time=now_time)
    formal = issue_company_statistic.objects.get(
        company="FacebookAI", flag=0).count
    issue_company_statistic.objects.filter(company="FacebookAI", flag=0).update(count=formal + facebookai_issue,
                                                                                total=formal_total,
                                                                                update_time=now_time)
    formal = issue_company_statistic.objects.get(
        company="GoogleLLC", flag=0).count
    issue_company_statistic.objects.filter(company="GoogleLLC", flag=0).update(count=formal + googlellc_issue,
                                                                               total=formal_total,
                                                                               update_time=now_time)
    formal = issue_company_statistic.objects.get(company="Intel", flag=0).count
    issue_company_statistic.objects.filter(company="Intel", flag=0).update(count=formal + intel_issue,
                                                                           total=formal_total,
                                                                           update_time=now_time)
    formal = issue_company_statistic.objects.get(
        company="NVIDIA", flag=0).count
    issue_company_statistic.objects.filter(company="NVIDIA", flag=0).update(count=formal + nvidia_issue,
                                                                            total=formal_total,
                                                                            update_time=now_time)
    formal = issue_company_statistic.objects.get(
        company="Hoofs&Horns,INC", flag=0).count
    issue_company_statistic.objects.filter(company="Hoofs&Horns,INC", flag=0).update(count=formal + hhinc_issue,
                                                                                     total=formal_total,
                                                                                     update_time=now_time)
    # ---------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------更新committer的company信息
    committer_formal = total.objects.get(source="committer").total
    committer_now = repo.get_commits().totalCount
    i = 0
    count = 0
    alibabainc_committer = 0
    quansight_committer = 0
    facebook_committer = 0
    pytorch_committer = 0
    anduril_committer = 0
    facebookai_committer = 0
    facebookair_committer = 0
    google_committer = 0
    hhinc_committer = 0
    intel_committer = 0
    mitcsail_committer = 0
    nvidia_committer = 0
    onnx_committer = 0
    commits = repo.get_commits().reversed
    for commit in commits:
        i = i + 1
        print(i)
        if i > committer_now - committer_formal:
            print("pytorch committer company update finish!")
            break
        else:
            if commit.author is None:
                a = 1
            else:
                if commit.author.company:
                    print(company_handle(commit.author.company))
                    count = count + 1
                    if "ALIBABAINC" in company_handle(commit.author.company):
                        alibabainc_committer = alibabainc_committer + 1
                    if "QUANSIGHT" in company_handle(commit.author.company):
                        quansight_committer = quansight_committer + 1
                    if "FACEBOOK" in company_handle(commit.author.company):
                        facebook_committer = facebook_committer + 1
                    if "PYTORCH" in company_handle(commit.author.company):
                        pytorch_committer = pytorch_committer + 1
                    if "Anduril" in company_handle(commit.author.company):
                        anduril_committer = anduril_committer + 1
                    if "FACEBOOKAI" in company_handle(commit.author.company):
                        facebookai_committer = facebookai_committer + 1
                    if "FACEBOOKAIRESEARCH" in company_handle(commit.author.company):
                        facebookair_committer = facebookair_committer + 1
                    if "GOOGLE" in company_handle(commit.author.company):
                        google_committer = google_committer + 1
                    if "HOOFSANDHORNSINC" in company_handle(commit.author.company):
                        hhinc_committer = hhinc_committer + 1
                    if "INTEL" in company_handle(commit.author.company):
                        intel_committer = intel_committer + 1
                    if "MITCSAIL" in company_handle(commit.author.company):
                        mitcsail_committer = mitcsail_committer + 1
                    if "NVIDIA" in company_handle(commit.author.company):
                        nvidia_committer = nvidia_committer + 1
                    if "ONNX" in company_handle(commit.author.company):
                        onnx_committer = onnx_committer + 1
                    committer_company.objects.create(node_id=commit.author.node_id,
                                                     company=company_handle(
                                                         commit.author.company),
                                                     get_time=now_time)
    formal_total = committer_company_statistic.objects.get(
        company="Facebook", flag=0).total
    formal_total = count + formal_total
    formal = committer_company_statistic.objects.get(
        company="Alibaba,INC", flag=0).count
    committer_company_statistic.objects.filter(company="Alibaba,INC", flag=0).update(
        count=formal + alibabainc_committer,
        total=formal_total, update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="Quansight", flag=0).count
    committer_company_statistic.objects.filter(company="Quansight", flag=0).update(count=formal + quansight_committer,
                                                                                   total=formal_total,
                                                                                   update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="Facebook", flag=0).count
    committer_company_statistic.objects.filter(company="Facebook", flag=0).update(count=formal + facebook_committer,
                                                                                  total=formal_total,
                                                                                  update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="Pytorch", flag=0).count
    committer_company_statistic.objects.filter(company="Pytorch", flag=0).update(count=formal + pytorch_committer,
                                                                                 total=formal_total,
                                                                                 update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="Anduril", flag=0).count
    committer_company_statistic.objects.filter(company="Anduril", flag=0).update(count=formal + anduril_committer,
                                                                                 total=formal_total,
                                                                                 update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="FacebookAI", flag=0).count
    committer_company_statistic.objects.filter(company="FacebookAI", flag=0).update(count=formal + facebookai_committer,
                                                                                    total=formal_total,
                                                                                    update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="FacebookAIResearch", flag=0).count
    committer_company_statistic.objects.filter(company="FacebookAIResearch", flag=0).update(
        count=formal + facebookair_committer,
        total=formal_total, update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="Google", flag=0).count
    committer_company_statistic.objects.filter(company="Google", flag=0).update(count=formal + google_committer,
                                                                                total=formal_total,
                                                                                update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="Intel", flag=0).count
    committer_company_statistic.objects.filter(company="Intel", flag=0).update(count=formal + intel_committer,
                                                                               total=formal_total,
                                                                               update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="MIT CSAIL", flag=0).count
    committer_company_statistic.objects.filter(company="MIT CSAIL", flag=0).update(count=formal + mitcsail_committer,
                                                                                   total=formal_total,
                                                                                   update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="NVIDIA", flag=0).count
    committer_company_statistic.objects.filter(company="NVIDIA", flag=0).update(count=formal + nvidia_committer,
                                                                                total=formal_total,
                                                                                update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="ONNX", flag=0).count
    committer_company_statistic.objects.filter(company="ONNX", flag=0).update(count=formal + onnx_committer,
                                                                              total=formal_total,
                                                                              update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="Hoofs&Horns,INC", flag=0).count
    committer_company_statistic.objects.filter(company="Hoofs&Horns,INC", flag=0).update(count=formal + hhinc_committer,
                                                                                         total=formal_total,
                                                                                         update_time=now_time)
    # ---------------------------------------------------------------------------------------------------
    # total.objects.filter(source='stargazer').update(total=stargazer_now)
    total.objects.filter(source='issue').update(total=issue_now)
    total.objects.filter(source='committer').update(total=committer_now)
    # ---------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------更新issue除star以外的相关信息
    issues = repo.get_issues().reversed
    i = 0
    for issue in issues:
        i = i + 1
        print(i)
        if pytorch_issues.objects.filter(id=issue.id).exists:
            print("pytorch issues data update finish!")
            break
        else:
            print(issue.created_at)
            print(issue.title)
            if issue.closed_at is None:
                pytorch_issues.objects.create(id=issue.id, created_at=issue.created_at, updated_at=issue.updated_at,
                                              comment_cnt=issue.comments, title=issue.title)
            else:
                pytorch_issues.objects.create(id=issue.id, created_at=issue.created_at, updated_at=issue.updated_at,
                                              closed_at=issue.closed_at,
                                              comment_cnt=issue.comments, title=issue.title)
    # ----------------------------------------------------------------------------------------------------
    return JsonResponse(response)


def pandas_issue(request):
    # ------------------------------获取issue的assignee信息（可全部获取）
    '''g = Github("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")  # 自己获取的github token
    repo = g.get_repo('pandas-dev/pandas')  # 获取pandas项目相关信息
    issues = repo.get_issues()
    print(issues.totalCount)
    now_time = dt.datetime.now().strftime('%F %T')
    i = 0
    for issue in issues:
        i = i + 1
        print(i)
        if i <= 0:
            continue
        else:
            if issue.assignee is None:
                a=1
            else:
                if issue.assignee.company:
                    print(company_handle(issue.assignee.company))
                    pandas_issue_company.objects.create(node_id=issue.assignee.node_id, company=company_handle(issue.assignee.company),
                                                     get_time=now_time)'''
    # -----------------------------------------------------------------------------
    '''context = HttpResponse(content_type='text/csv')  # 告诉浏览器是text/csv格式
    context['Content-Disposition'] = 'attachment; filename="pandas_issue_company_statistic.csv"'  # csv文件名，不影响
    writer = csv.writer(context)
    writer.writerow(['company', 'count', 'total', 'update_time'])
    for info in pandas_issue_company_statistic.objects.all():
        writer.writerow([info.company, info.count, info.total, info.update_time])
    # return response
    print(context)
    return context'''
    response = {}
    return JsonResponse(response)


def pandas_committer(request):
    '''g = Github("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")  # 自己获取的github token
    repo = g.get_repo('pandas-dev/pandas')  # 获取pandas项目相关信息
    commits = repo.get_commits().reversed
    print(commits.totalCount)
    now_time = dt.datetime.now().strftime('%F %T')
    i = 0
    for commit in commits:
        i = i + 1
        print(i)
        if i>commits.totalCount-17274: break
        if i <= 13263:
            continue
        else:
            if commit.author is None:
                a = 1
            else:
                if commit.author.company:
                    print(company_handle(commit.author.company))
                    committer_company.objects.create(node_id=commit.author.node_id,
                                                     company=company_handle(commit.author.company),
                                                     get_time=now_time)'''
    '''context = HttpResponse(content_type='text/csv')  # 告诉浏览器是text/csv格式
    context['Content-Disposition'] = 'attachment; filename="pandas_committer_company_statistic.csv"'  # csv文件名，不影响
    writer = csv.writer(context)
    writer.writerow(['company', 'count', 'total', 'update_time'])
    for info in pandas_committer_company_statistic.objects.all():
        writer.writerow([info.company, info.count, info.total, info.update_time])
    # return response
    print(context)
    return context'''
    response = {}
    return JsonResponse(response)


def pandas_update(request):
    response = {}
    g = Github("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")  # 自己获取的github token
    repo = g.get_repo('pandas-dev/pandas')  # 获取pytorch项目相关信息
    now_time = dt.datetime.now().strftime('%F %T')
    # -------------------------------------------更新star_gazer的company信息
    stargazer_formal = pandas_total.objects.get(source="stargazer").total
    stargazer_now = repo.stargazers_count
    stargazers1 = repo.get_stargazers().reversed
    i = 0
    count = 0
    amazon_star = 0
    google_star = 0
    facebook_star = 0
    alibaba_star = 0
    bytedance_star = 0
    tencent_star = 0
    ibm_star = 0
    pku_star = 0
    baidu_star = 0
    intel_star = 0
    meta_star = 0
    nubank_star = 0
    vm_star = 0
    zju_star = 0
    for people in stargazers1:
        i = i + 1
        print(i)
        if i > stargazer_now - stargazer_formal:
            print("pandas stargazer company update finish!")
            break
        if people.company:
            print(company_handle(people.company))
            count = count + 1
            if "AMAZON" in company_handle(people.company):
                amazon_star = amazon_star + 1
            if "GOOGLE" in company_handle(people.company):
                google_star = google_star + 1
            if "FACEBOOK" in company_handle(people.company):
                facebook_star = facebook_star + 1
            if "ALIBABA" in company_handle(people.company):
                alibaba_star = alibaba_star + 1
            if "BYTEDANCE" in company_handle(people.company):
                bytedance_star = bytedance_star + 1
            if "TENCENT" in company_handle(people.company):
                tencent_star = tencent_star + 1
            if "IBM" in company_handle(people.company):
                ibm_star = ibm_star + 1
            if "PEKINGUNIVERSITY" in company_handle(people.company):
                pku_star = pku_star + 1
            if "BAIDU" in company_handle(people.company):
                baidu_star = baidu_star + 1
            if "INTEL" in company_handle(people.company):
                intel_star = intel_star + 1
            if "META" in company_handle(people.company):
                meta_star = meta_star + 1
            if "NUBANK" in company_handle(people.company):
                nubank_star = nubank_star + 1
            if "VMWARE" in company_handle(people.company):
                vm_star = vm_star + 1
            if "ZHEJIANGUNIVERSITY" in company_handle(people.company):
                zju_star = zju_star + 1
            pandas_stargazer_company.objects.create(node_id=people.node_id, company=company_handle(people.company),
                                                    get_time=now_time)
    formal_total = stargazer_company_statistic.objects.get(
        company="Amazon", flag=1).total
    formal_total = count + formal_total
    formal = stargazer_company_statistic.objects.get(
        company="Amazon", flag=1).count
    stargazer_company_statistic.objects.filter(company="Amazon", flag=1).update(count=formal + amazon_star,
                                                                                total=formal_total,
                                                                                update_time=now_time)
    formal = stargazer_company_statistic.objects.get(
        company="Google", flag=1).count
    stargazer_company_statistic.objects.filter(company="Google", flag=1).update(count=formal + google_star,
                                                                                total=formal_total,
                                                                                update_time=now_time)
    formal = stargazer_company_statistic.objects.get(
        company="Facebook", flag=1).count
    stargazer_company_statistic.objects.filter(company="Facebook", flag=1).update(count=formal + facebook_star,
                                                                                  total=formal_total,
                                                                                  update_time=now_time)
    formal = stargazer_company_statistic.objects.get(
        company="Alibaba", flag=1).count
    stargazer_company_statistic.objects.filter(company="Alibaba", flag=1).update(count=formal + alibaba_star,
                                                                                 total=formal_total,
                                                                                 update_time=now_time)
    formal = stargazer_company_statistic.objects.get(
        company="ByteDance", flag=1).count
    stargazer_company_statistic.objects.filter(company="ByteDance", flag=1).update(count=formal + bytedance_star,
                                                                                   total=formal_total,
                                                                                   update_time=now_time)
    formal = stargazer_company_statistic.objects.get(
        company="Tencent", flag=1).count
    stargazer_company_statistic.objects.filter(company="Tencent", flag=1).update(count=formal + tencent_star,
                                                                                 total=formal_total,
                                                                                 update_time=now_time)
    formal = stargazer_company_statistic.objects.get(
        company="IBM", flag=1).count
    stargazer_company_statistic.objects.filter(company="IBM", flag=1).update(count=formal + ibm_star,
                                                                             total=formal_total,
                                                                             update_time=now_time)
    formal = stargazer_company_statistic.objects.get(
        company="PekingUniversity", flag=1).count
    stargazer_company_statistic.objects.filter(company="PekingUniversity", flag=1).update(count=formal + pku_star,
                                                                                          total=formal_total,
                                                                                          update_time=now_time)
    formal = stargazer_company_statistic.objects.get(
        company="Baidu", flag=1).count
    stargazer_company_statistic.objects.filter(company="Baidu", flag=1).update(count=formal + baidu_star,
                                                                               total=formal_total,
                                                                               update_time=now_time)
    formal = stargazer_company_statistic.objects.get(
        company="Intel", flag=1).count
    stargazer_company_statistic.objects.filter(company="Intel", flag=1).update(count=formal + intel_star,
                                                                               total=formal_total,
                                                                               update_time=now_time)
    formal = stargazer_company_statistic.objects.get(
        company="Meta", flag=1).count
    stargazer_company_statistic.objects.filter(company="Meta", flag=1).update(count=formal + meta_star,
                                                                              total=formal_total,
                                                                              update_time=now_time)
    formal = stargazer_company_statistic.objects.get(
        company="Nubank", flag=1).count
    stargazer_company_statistic.objects.filter(company="Nubank", flag=1).update(count=formal + nubank_star,
                                                                                total=formal_total,
                                                                                update_time=now_time)
    formal = stargazer_company_statistic.objects.get(
        company="VMware", flag=1).count
    stargazer_company_statistic.objects.filter(company="VMware", flag=1).update(count=formal + vm_star,
                                                                                total=formal_total,
                                                                                update_time=now_time)
    formal = stargazer_company_statistic.objects.get(
        company="ZhejiangUniversity", flag=1).count
    stargazer_company_statistic.objects.filter(company="ZhejiangUniversity", flag=1).update(count=formal + zju_star,
                                                                                            total=formal_total,
                                                                                            update_time=now_time)
    # -----------------------------------------------------------------------------------------------------
    # --------------------------------------------------------更新issue的company信息
    issue_formal = pandas_total.objects.get(source="issue").total
    issue_now = repo.get_issues().totalCount
    issues = repo.get_issues().reversed
    i = 0
    count = 0
    c8451_issue = 0
    factor_issue = 0
    farfetch_issue = 0
    pandas_issue1 = 0
    vol_issue = 0
    zonos_issue = 0
    zyppio_issue = 0
    for issue in issues:
        i = i + 1
        print(i)
        if i > issue_now - issue_formal:
            print("pandas issue company update finish!")
            break
        if issue.assignee is None:
            a = 1
        else:
            if issue.assignee.company:
                print(company_handle(issue.assignee.company))
                count = count + 1
                if "8451" in company_handle(issue.assignee.company):
                    c8451_issue = c8451_issue + 1
                if "FACTOREDAI" in company_handle(issue.assignee.company):
                    factor_issue = factor_issue + 1
                if "FARFETCH" in company_handle(issue.assignee.company):
                    farfetch_issue = farfetch_issue + 1
                if "PANDASDEV" in company_handle(issue.assignee.company):
                    pandas_issue1 = pandas_issue1 + 1
                if "VOLTRONDATA" in company_handle(issue.assignee.company):
                    vol_issue = vol_issue + 1
                if "ZONOS" in company_handle(issue.assignee.company):
                    zonos_issue = zonos_issue + 1
                if "ZYPPIO" in company_handle(issue.assignee.company):
                    zyppio_issue = zyppio_issue + 1
                pandas_issue_company.objects.create(node_id=issue.assignee.node_id,
                                                    company=company_handle(
                                                        issue.assignee.company),
                                                    get_time=now_time)
    formal_total = issue_company_statistic.objects.get(
        company="Farfetch", flag=1).total
    formal_total = count + formal_total
    formal = issue_company_statistic.objects.get(
        company="84.51°", flag=1).count
    issue_company_statistic.objects.filter(company="84.51°", flag=1).update(count=formal + c8451_issue,
                                                                            total=formal_total, update_time=now_time)
    formal = issue_company_statistic.objects.get(
        company="Factored AI", flag=1).count
    issue_company_statistic.objects.filter(company="Factored AI", flag=1).update(count=formal + factor_issue,
                                                                                 total=formal_total,
                                                                                 update_time=now_time)
    formal = issue_company_statistic.objects.get(
        company="Farfetch", flag=1).count
    issue_company_statistic.objects.filter(company="Farfetch", flag=1).update(count=formal + farfetch_issue,
                                                                              total=formal_total, update_time=now_time)
    formal = issue_company_statistic.objects.get(
        company="PandasDev", flag=1).count
    issue_company_statistic.objects.filter(company="PandasDev", flag=1).update(count=formal + pandas_issue1,
                                                                               total=formal_total, update_time=now_time)
    formal = issue_company_statistic.objects.get(
        company="Voltron Data", flag=1).count
    issue_company_statistic.objects.filter(company="Voltron Data", flag=1).update(count=formal + vol_issue,
                                                                                  total=formal_total,
                                                                                  update_time=now_time)
    formal = issue_company_statistic.objects.get(company="Zonos", flag=1).count
    issue_company_statistic.objects.filter(company="Zonos", flag=1).update(count=formal + zonos_issue,
                                                                           total=formal_total, update_time=now_time)
    formal = issue_company_statistic.objects.get(
        company="Zyppio", flag=1).count
    issue_company_statistic.objects.filter(company="Zyppio", flag=1).update(count=formal + zyppio_issue,
                                                                            total=formal_total,
                                                                            update_time=now_time)
    # ---------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------更新committer的company信息
    committer_formal = pandas_total.objects.get(source="committer").total
    committer_now = repo.get_commits().totalCount
    i = 0
    count = 0
    c8451_committer = 0
    quansight_committer = 0
    dlr_committer = 0
    hca_committer = 0
    innobi_committer = 0
    microsoft_committer = 0
    palantir_committer = 0
    google_committer = 0
    pandas_committer1 = 0
    pytho_committer = 0
    rapids_committer = 0
    tubi_committer = 0
    vol_committer = 0
    was_committer = 0
    commits = repo.get_commits().reversed
    for commit in commits:
        i = i + 1
        print(i)
        if i > committer_now - committer_formal:
            print("pandas committer company update finish!")
            break
        else:
            if commit.author is None:
                a = 1
            else:
                if commit.author.company:
                    print(company_handle(commit.author.company))
                    count = count + 1
                    if "8451" in company_handle(commit.author.company):
                        c8451_committer = c8451_committer + 1
                    if "QUANSIGHT" in company_handle(commit.author.company):
                        quansight_committer = quansight_committer + 1
                    if "DLR" in company_handle(commit.author.company):
                        dlr_committer = dlr_committer + 1
                    if "HCAHEALTHCARE" in company_handle(commit.author.company):
                        hca_committer = hca_committer + 1
                    if "INNOBI" in company_handle(commit.author.company):
                        innobi_committer = innobi_committer + 1
                    if "MICROSOFT" in company_handle(commit.author.company):
                        microsoft_committer = microsoft_committer + 1
                    if "PALANTIRTECHNOLOGIES" in company_handle(commit.author.company):
                        palantir_committer = palantir_committer + 1
                    if "GOOGLE" in company_handle(commit.author.company):
                        google_committer = google_committer + 1
                    if "PANDASDEV" in company_handle(commit.author.company):
                        pandas_committer1 = pandas_committer1 + 1
                    if "PYTHOMATION" in company_handle(commit.author.company):
                        pytho_committer = pytho_committer + 1
                    if "RAPIDSAI" in company_handle(commit.author.company):
                        rapids_committer = rapids_committer + 1
                    if "TUBITV" in company_handle(commit.author.company):
                        tubi_committer = tubi_committer + 1
                    if "VOLTRONDATA" in company_handle(commit.author.company):
                        vol_committer = vol_committer + 1
                    if "WASHINGTONUNIVERSITYINSTLOUIS" in company_handle(commit.author.company):
                        was_committer = was_committer + 1
                    pandas_committer_company.objects.create(node_id=commit.author.node_id,
                                                            company=company_handle(
                                                                commit.author.company),
                                                            get_time=now_time)
    formal_total = committer_company_statistic.objects.get(
        company="DLR", flag=1).total
    formal_total = count + formal_total
    formal = committer_company_statistic.objects.get(
        company="84.51°", flag=1).count
    committer_company_statistic.objects.filter(company="84.51°", flag=1).update(count=formal + c8451_committer,
                                                                                total=formal_total,
                                                                                update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="Quansight", flag=1).count
    committer_company_statistic.objects.filter(company="Quansight", flag=1).update(count=formal + quansight_committer,
                                                                                   total=formal_total,
                                                                                   update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="DLR", flag=1).count
    committer_company_statistic.objects.filter(company="DLR", flag=1).update(count=formal + dlr_committer,
                                                                             total=formal_total, update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="HCA Healthcare", flag=1).count
    committer_company_statistic.objects.filter(company="HCA Healthcare", flag=1).update(count=formal + hca_committer,
                                                                                        total=formal_total,
                                                                                        update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="Innobi", flag=1).count
    committer_company_statistic.objects.filter(company="Innobi", flag=1).update(count=formal + innobi_committer,
                                                                                total=formal_total,
                                                                                update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="Microsoft", flag=1).count
    committer_company_statistic.objects.filter(company="Microsoft", flag=1).update(count=formal + microsoft_committer,
                                                                                   total=formal_total,
                                                                                   update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="Palantir Technologies", flag=1).count
    committer_company_statistic.objects.filter(company="Palantir Technologies", flag=1).update(
        count=formal + palantir_committer,
        total=formal_total, update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="Google", flag=1).count
    committer_company_statistic.objects.filter(company="Google", flag=1).update(count=formal + google_committer,
                                                                                total=formal_total,
                                                                                update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="Pythomation", flag=1).count
    committer_company_statistic.objects.filter(company="Pythomation", flag=1).update(count=formal + pytho_committer,
                                                                                     total=formal_total,
                                                                                     update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="RAPIDS AI", flag=1).count
    committer_company_statistic.objects.filter(company="RAPIDS AI", flag=1).update(count=formal + rapids_committer,
                                                                                   total=formal_total,
                                                                                   update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="Tubi TV", flag=1).count
    committer_company_statistic.objects.filter(company="Tubi TV", flag=1).update(count=formal + tubi_committer,
                                                                                 total=formal_total,
                                                                                 update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="Voltron Data", flag=1).count
    committer_company_statistic.objects.filter(company="Voltron Data", flag=1).update(count=formal + vol_committer,
                                                                                      total=formal_total,
                                                                                      update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="PandasDev", flag=1).count
    committer_company_statistic.objects.filter(company="PandasDev", flag=1).update(count=formal + pandas_committer1,
                                                                                   total=formal_total,
                                                                                   update_time=now_time)
    formal = committer_company_statistic.objects.get(
        company="WashingtonUniversityinStLouis", flag=1).count
    committer_company_statistic.objects.filter(company="WashingtonUniversityinStLouis", flag=1).update(
        count=formal + was_committer,
        total=formal_total,
        update_time=now_time)
    # ---------------------------------------------------------------------------------------------------
    pandas_total.objects.filter(source='stargazer').update(total=stargazer_now)
    pandas_total.objects.filter(source='issue').update(total=issue_now)
    pandas_total.objects.filter(source='committer').update(total=committer_now)
    # ---------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------更新issue除star以外的相关信息
    issues = repo.get_issues().reversed
    i = 0
    for issue in issues:
        i = i + 1
        print(i)
        if pandas_issues.objects.filter(id=issue.id).exists:
            print("pandas issues data update finish!")
            break
        else:
            print(issue.created_at)
            print(issue.title)
            if issue.closed_at is None:
                pandas_issues.objects.create(id=issue.id, created_at=issue.created_at, updated_at=issue.updated_at,
                                             comment_cnt=issue.comments, title=issue.title)
            else:
                pandas_issues.objects.create(id=issue.id, created_at=issue.created_at, updated_at=issue.updated_at,
                                             closed_at=issue.closed_at,
                                             comment_cnt=issue.comments, title=issue.title)
    # ----------------------------------------------------------------------------------------------------
    return JsonResponse(response)


def about_us(request):
    commit_users = []
    commit_users.append({"name": "陈奕宇", "user": "radioactivecyy", "url": "https://github.com/radioactivecyy",
                         "a_url": "https://avatars.githubusercontent.com/u/81542105?v=4"})
    # return JsonResponse(commit_users)
    return render(request, 'about-us.html', {"us": commit_users})


# the git log command used
def git_log_to_file(pytorch="/Users/ihsiao/Documents/SRE/pytorch",
                    outputdir="data/_new.txt",
                    instruction='''--shortstat --pretty=format:"@COMMIT@ %H @AUTHOR@ %an <%ae> @CONTENT@ %s @TIME@ %ad @C_TIME@ %cd @COMMITTER@ %cn <%ce>"''',
                    from_time=None):
    order_string = "git log " + instruction
    if from_time:
        order_string += ''' --after="''' + from_time.strftime("%Y-%m-%d %H:%M:%S") + '" '
    order_string += " > " + os.path.join(os.getcwd(), outputdir)
    prev_dir = os.getcwd()
    os.chdir(pytorch)
    print(order_string)
    os.system(order_string)
    os.chdir(prev_dir)


def pandas_commit_git_log_parser(input_filename: str):
    info_template = re.compile(r"@COMMIT@ (.*?) @AUTHOR@ (.*?) <(.*?)> @CONTENT@ (.*?) @TIME@ (.*?) @C_TIME@ (.*?) "
                               r"@COMMITTER@ (.*?) <(.*?)>")
    del_template = re.compile(r"(\d+) deletion")
    ins_template = re.compile(r"(\d+) insertion")
    file_template = re.compile(r"(\d+) file")

    infile = open(input_filename, encoding='utf-8')
    filebuf = infile.readlines()
    filebuf_i = 0

    finished_cnt = 0
    while filebuf_i < len(filebuf):
        info_resolved = re.findall(info_template, filebuf[filebuf_i])  # extract each fields
        if info_resolved:  # if succeeded
            pandas_commit_entry = pandas_commit_history()  # new entry to be inserted

            # 更新/创建贡献者表单项
            try:
                author_entry = pandas_commit_contributors.objects.get(author=info_resolved[0][1])
            except pandas_commit_contributors.DoesNotExist:
                author_entry = pandas_commit_contributors(author=info_resolved[0][1])
            # author_entry.save()

            # 添加直接获取的信息
            pandas_commit_entry.hash = info_resolved[0][0]
            pandas_commit_entry.author = author_entry
            pandas_commit_entry.author_email = info_resolved[0][2]
            pandas_commit_entry.commit_intro = info_resolved[0][3][:500]
            pandas_commit_entry.time_local = datetime.strptime(info_resolved[0][4][-19:-11], "%H:%M:%S")
            pandas_commit_entry.commit_time = datetime.strptime(info_resolved[0][5][:-6], "%a %b %d %H:%M:%S %Y")
            pandas_commit_entry.committer = info_resolved[0][6]
            pandas_commit_entry.committer_email = info_resolved[0][7]

            # 分析是否是设计相关的讨论
            pandas_commit_entry.if_design = check_if_design_related(info_resolved[0][3])
            print(pandas_commit_entry.commit_time)
            # 插入本次commit更改的统计数据（如有）
            try:
                if filebuf[filebuf_i + 1][0] == ' ':  # file change stat exists
                    filebuf_i += 3

                    # reading modification stats
                    modi_raw = filebuf[filebuf_i - 2]
                    if del_resolved := re.findall(del_template, modi_raw):
                        pandas_commit_entry.modi_del = int(del_resolved[0])
                    else:
                        pandas_commit_entry.modi_del = 0

                    if ins_resolved := re.findall(ins_template, modi_raw):
                        pandas_commit_entry.modi_ins = int(ins_resolved[0])
                    else:
                        pandas_commit_entry.modi_ins = 0

                    if file_resolved := re.findall(file_template, modi_raw):
                        pandas_commit_entry.modi_files = int(file_resolved[0])
                    else:
                        pandas_commit_entry.modi_files = 0

                else:  # no file change
                    filebuf_i += 1
                    pandas_commit_entry.modi_del = 0
                    pandas_commit_entry.modi_ins = 0
                    pandas_commit_entry.modi_files = 0
            except IndexError:
                break

            # 完成贡献者表单
            author_entry.modi_ins += pandas_commit_entry.modi_ins
            author_entry.modi_del += pandas_commit_entry.modi_del
            author_entry.modi_files += pandas_commit_entry.modi_files
            author_entry.save()

            # 完成pandas_commit_history表单
            pandas_commit_entry.save()
            finished_cnt += 1
        else:
            filebuf_i += 1
    infile.close()


def commit_git_log_parser(input_filename: str):
    info_template = re.compile(r"@COMMIT@ (.*?) @AUTHOR@ (.*?) <(.*?)> @CONTENT@ (.*?) @TIME@ (.*?) @C_TIME@ (.*?) "
                               r"@COMMITTER@ (.*?) <(.*?)>")
    del_template = re.compile(r"(\d+) deletion")
    ins_template = re.compile(r"(\d+) insertion")
    file_template = re.compile(r"(\d+) file")

    infile = open(input_filename, encoding='utf-8')
    filebuf = infile.readlines()
    filebuf_i = 0

    finished_cnt = 0
    while filebuf_i < len(filebuf):
        info_resolved = re.findall(info_template, filebuf[filebuf_i])  # extract each fields
        if info_resolved:  # if succeeded
            commit_entry = commit_history()  # new entry to be inserted

            # 更新/创建贡献者表单项
            try:
                author_entry = commit_contributors.objects.get(author=info_resolved[0][1])
            except commit_contributors.DoesNotExist:
                author_entry = commit_contributors(author=info_resolved[0][1])
            author_entry.save()

            # 添加直接获取的信息
            commit_entry.hash = info_resolved[0][0]
            commit_entry.author = author_entry
            commit_entry.author_email = info_resolved[0][2]
            commit_entry.commit_intro = info_resolved[0][3][:500]
            commit_entry.time_local = datetime.strptime(info_resolved[0][4][-19:-11], "%H:%M:%S")
            commit_entry.commit_time = datetime.strptime(info_resolved[0][5][:-6], "%a %b %d %H:%M:%S %Y")
            commit_entry.committer = info_resolved[0][6]
            commit_entry.committer_email = info_resolved[0][7]

            # 分析是否是设计相关的讨论
            commit_entry.if_design = check_if_design_related(info_resolved[0][3])

            # 插入本次commit更改的统计数据（如有）
            try:
                if filebuf[filebuf_i + 1][0] == ' ':  # file change stat exists
                    filebuf_i += 3

                    # reading modification stats
                    modi_raw = filebuf[filebuf_i - 2]
                    if del_resolved := re.findall(del_template, modi_raw):
                        commit_entry.modi_del = int(del_resolved[0])
                    else:
                        commit_entry.modi_del = 0

                    if ins_resolved := re.findall(ins_template, modi_raw):
                        commit_entry.modi_ins = int(ins_resolved[0])
                    else:
                        commit_entry.modi_ins = 0

                    if file_resolved := re.findall(file_template, modi_raw):
                        commit_entry.modi_files = int(file_resolved[0])
                    else:
                        commit_entry.modi_files = 0

                else:  # no file change
                    filebuf_i += 1
                    commit_entry.modi_del = 0
                    commit_entry.modi_ins = 0
                    commit_entry.modi_files = 0
            except IndexError:
                break

            # 完成贡献者表单
            author_entry.modi_ins += commit_entry.modi_ins
            author_entry.modi_del += commit_entry.modi_del
            author_entry.modi_files += commit_entry.modi_files
            author_entry.save()

            # 完成commit_history表单
            commit_entry.save()
            finished_cnt += 1
        else:
            filebuf_i += 1
    infile.close()


def check_if_design_related(intro: str):
    intro = intro.lower()
    common_labels = "add,fix,er,better,func,dynamo,reland,fsdp,primtorch,quant,executorch,api,functorch,onnx,dict,inductor,xnn,nnc,mps"
    platforms = "macos,os x,linux,ubuntu,centos,debian,gentoo,fedora,arch,opensuse,windows,dos,80486,i386,i486,i586," \
                "i686,x86,x64,arm,nvidia"
    robustness = "robust,strong,vigorous,sturdy,tough,powerful,solidly,muscular,sinewy,rugged,hardy,danger,shield," \
                 "shelter,guard,defend,secure,allright,unsafe,insecure,risk"

    if any([w in intro and w for w in common_labels.split(',')]):
        # if contains keywords of common labels
        return True
    elif any([w in intro and w for w in platforms.split(',')]):
        # if contains keywords of platforms
        return True
    elif any([w in intro and w for w in robustness.split(',')]):
        # if contains keywords of robustness
        return True
    else:
        # none of above, not design-related
        return False


def commit_update_main(request):
    # 检查更新记录
    try:
        # 存在更新记录，取得最新一条commit的时间
        last_upd = commit_update.objects.order_by('time_last_record').last().time_last_record
    except Exception:
        last_upd = None
    print(last_upd)
    # 执行更新

    # 此处将`_pytorch`更换为服务器中的pytorch仓库地址
    # _pytorch = "/Users/ihsiao/Documents/SRE/pytorch"

    # 此处将`_outputdir`更换为输出文本文件的路径
    # _outputdir = "data/_amendment.txt"

    # 获得git log
    # git_log_to_file(pytorch=_pytorch, from_time=last_upd, outputdir=_outputdir)

    # 从文本文件读取git log，分析并存入数据库
    # commit_git_log_parser("data/_amendment.txt")

    # 重新计算从上一次的最后一条记录开始所有日期的统计数据
    if not last_upd:  # 若是第一次更新，则全部重新计算
        try:
            last_upd = commit_history.objects.order_by('commit_time').first().commit_time
        except commit_history.DoesNotExist:
            # 没有任何记录，返回
            print("NO VALID RECORDS IN COMMIT_HISTORY!")
            return

    # 对齐到当日00:00:00
    last_upd = datetime(last_upd.year, last_upd.month, last_upd.day)

    # 聚合搜索三个统计值，每日commit数、设计讨论数和总文件更改数量
    _comm_cnt = commit_history.objects.filter(commit_time__gt=last_upd).annotate(
        date=TruncDate('commit_time')).values('date').annotate(nums=Count('hash'))

    _desi_cnt = commit_history.objects.filter(commit_time__gt=last_upd, if_design=True).annotate(
        date=TruncDate('commit_time')).values('date').annotate(nums=Count('hash'))

    _modi_files = commit_history.objects.filter(commit_time__gt=last_upd).annotate(
        date=TruncDate('commit_time')).values('date').annotate(nums=Sum('modi_files'))

    # 主要贡献者的上述三个值

    _comm_cnt_core = commit_history.objects.filter(commit_time__gt=last_upd,
                                                   author__if_core=True).annotate(
        date=TruncDate('commit_time')).values('date').annotate(nums=Count('hash'))

    _desi_cnt_core = commit_history.objects.filter(commit_time__gt=last_upd, if_design=True,
                                                   author__if_core=True).annotate(
        date=TruncDate('commit_time')).values('date').annotate(nums=Count('hash'))

    _modi_files_core = commit_history.objects.filter(commit_time__gt=last_upd,
                                                     author__if_core=True).annotate(
        date=TruncDate('commit_time')).values('date').annotate(nums=Sum('modi_files'))

    # 遍历过程中的日期
    begin_date = last_upd
    end_date = datetime.now()

    while begin_date <= end_date:
        print(begin_date)
        try:
            date_entry = commit_by_day.objects.get(date=begin_date)
        except commit_by_day.DoesNotExist:
            date_entry = commit_by_day()
            date_entry.date = begin_date
        try:
            # 在每个日期中分别添加三个聚合字典中的对应值
            date_entry.comm_cnt = _comm_cnt.get(date=TruncDate(begin_date))['nums']
            date_entry.desi_cnt = _desi_cnt.get(date=TruncDate(begin_date))['nums']
            date_entry.modi_files = _modi_files.get(date=TruncDate(begin_date))['nums']
            # 在每个日期中分别添加三个聚合字典中的对应值（核心贡献者）
            date_entry.comm_cnt_core = _comm_cnt_core.get(date=TruncDate(begin_date))['nums']
            date_entry.desi_cnt_core = _desi_cnt_core.get(date=TruncDate(begin_date))['nums']
            date_entry.modi_files_core = _modi_files_core.get(date=TruncDate(begin_date))['nums']
        except Exception:  # 缺少本日记录，计为0
            date_entry.comm_cnt = 0
            date_entry.desi_cnt = 0
            date_entry.modi_files = 0
            date_entry.comm_cnt_core = 0
            date_entry.desi_cnt_core = 0
            date_entry.modi_files_core = 0
            date_entry.modi_ins = '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
            date_entry.modi_del = '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
        # 对分小时的数据进行统计，统计增加和减少的行数
        #
        # # 删除的行数
        # del_set = commit_history.objects.annotate(date=TruncDate('commit_time')).filter(date=begin_date).annotate(
        # 	hour=ExtractHour('time_local')).values('hour').annotate(nums=Sum('modi_del'))
        # del_str = ""
        # for _h in range(24):
        # 	if _h is not 0:
        # 		del_str += ","
        # 	try:
        # 		stat = del_set.get(hour=str(_h))['nums']
        # 	except Exception:
        # 		stat = 0
        # 	del_str += str(stat)
        # date_entry.modi_del = del_str
        #
        # # 添加的行数
        # ins_set = commit_history.objects.annotate(date=TruncDate('commit_time')).filter(date=begin_date).annotate(
        # 	hour=ExtractHour('time_local')).values('hour').annotate(nums=Sum('modi_ins'))
        # ins_str = ""
        # for _h in range(24):
        # 	if _h is not 0:
        # 		ins_str += ","
        # 	try:
        # 		stat = ins_set.get(hour=str(_h))['nums']
        # 	except Exception:
        # 		stat = 0
        # 	ins_str += str(stat)
        # date_entry.modi_ins = ins_str

        # print(date_entry.date, date_entry.comm_cnt, date_entry.desi_cnt, date_entry.modi_files)

        # 保存对每一项的更改
        date_entry.save()
        begin_date += dt.timedelta(days=1)

    # 记录更新
    current_upd = commit_update()
    current_upd.time_update = datetime.now()
    current_upd.time_last_record = commit_history.objects.latest('commit_time').commit_time
    current_upd.save()
    return JsonResponse({'current_upd': current_upd.time_update})


def commit_update_byhour(_from: datetime):
    # 对齐到当日00:00:00
    last_upd = datetime(_from.year, _from.month, _from.day)

    # 遍历过程中的日期
    begin_date = last_upd
    end_date = datetime.now()

    while begin_date <= end_date:
        print(begin_date)
        try:
            date_entry = commit_by_day.objects.get(date=begin_date)
        except commit_by_day.DoesNotExist:
            date_entry = commit_by_day()
            date_entry.date = begin_date
            date_entry.modi_ins = '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
            date_entry.modi_del = '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'

        # 对分小时的数据进行统计，统计增加和减少的行数

        # 删除的行数
        del_set = commit_history.objects.annotate(date=TruncDate('commit_time')).filter(date=begin_date).annotate(
            hour=ExtractHour('time_local')).values('hour').annotate(nums=Sum('modi_del'))
        del_str = ""
        for _h in range(24):
            if _h != 0:
                del_str += ","
            try:
                stat = del_set.get(hour=str(_h))['nums']
            except Exception:
                stat = 0
            del_str += str(stat)
        date_entry.modi_del = del_str

        # 添加的行数
        ins_set = commit_history.objects.annotate(date=TruncDate('commit_time')).filter(date=begin_date).annotate(
            hour=ExtractHour('time_local')).values('hour').annotate(nums=Sum('modi_ins'))
        ins_str = ""
        for _h in range(24):
            if _h != 0:
                ins_str += ","
            try:
                stat = ins_set.get(hour=str(_h))['nums']
            except Exception:
                stat = 0
            ins_str += str(stat)
        date_entry.modi_ins = ins_str

        # print(date_entry.date, date_entry.comm_cnt, date_entry.desi_cnt, date_entry.modi_files)

        # 保存对每一项的更改
        date_entry.save()
        begin_date += dt.timedelta(days=1)

    # 记录更新
    current_upd = commit_update()
    current_upd.time_update = datetime.now()
    current_upd.time_last_record = commit_history.objects.latest('commit_time').commit_time
    current_upd.save()


def pandas_commit_update_main(request):
    # 检查更新记录
    try:
        # 存在更新记录，取得最新一条commit的时间
        last_upd = pandas_commit_update.objects.order_by('time_last_record').last().time_last_record
    except Exception:
        last_upd = None
    print(last_upd)
    # 执行更新

    # 此处将`_pytorch`更换为服务器中的pytorch仓库地址
    # _pytorch = "/Users/ihsiao/Documents/SRE/pytorch"

    # 此处将`_outputdir`更换为输出文本文件的路径
    # _outputdir = "data/_amendment.txt"

    # 获得git log
    # git_log_to_file(pytorch=_pytorch, from_time=last_upd, outputdir=_outputdir)

    # 从文本文件读取git log，分析并存入数据库
    # pandas_commit_git_log_parser("data/_amendment.txt")

    # 重新计算从上一次的最后一条记录开始所有日期的统计数据
    if not last_upd:  # 若是第一次更新，则全部重新计算
        try:
            last_upd = pandas_commit_history.objects.order_by('commit_time').first().commit_time
        except pandas_commit_history.DoesNotExist:
            # 没有任何记录，返回
            print("NO VALID RECORDS IN pandas_commit_HISTORY!")
            return

    # 对齐到当日00:00:00
    last_upd = datetime(last_upd.year, last_upd.month, last_upd.day)

    # 聚合搜索三个统计值，每日commit数、设计讨论数和总文件更改数量
    _comm_cnt = pandas_commit_history.objects.filter(commit_time__gt=last_upd).annotate(
        date=TruncDate('commit_time')).values('date').annotate(nums=Count('hash'))

    _desi_cnt = pandas_commit_history.objects.filter(commit_time__gt=last_upd, if_design=True).annotate(
        date=TruncDate('commit_time')).values('date').annotate(nums=Count('hash'))

    _modi_files = pandas_commit_history.objects.filter(commit_time__gt=last_upd).annotate(
        date=TruncDate('commit_time')).values('date').annotate(nums=Sum('modi_files'))

    # 主要贡献者的上述三个值

    _comm_cnt_core = pandas_commit_history.objects.filter(commit_time__gt=last_upd,
                                                          author__if_core=True).annotate(
        date=TruncDate('commit_time')).values('date').annotate(nums=Count('hash'))

    _desi_cnt_core = pandas_commit_history.objects.filter(commit_time__gt=last_upd, if_design=True,
                                                          author__if_core=True).annotate(
        date=TruncDate('commit_time')).values('date').annotate(nums=Count('hash'))

    _modi_files_core = pandas_commit_history.objects.filter(commit_time__gt=last_upd,
                                                            author__if_core=True).annotate(
        date=TruncDate('commit_time')).values('date').annotate(nums=Sum('modi_files'))

    # 遍历过程中的日期
    begin_date = last_upd
    end_date = datetime.now()

    while begin_date <= end_date:
        print(begin_date)
        try:
            date_entry = pandas_commit_by_day.objects.get(date=begin_date)
        except pandas_commit_by_day.DoesNotExist:
            date_entry = pandas_commit_by_day()
            date_entry.date = begin_date
        try:
            # 在每个日期中分别添加三个聚合字典中的对应值
            date_entry.comm_cnt = _comm_cnt.get(date=TruncDate(begin_date))['nums']
            date_entry.desi_cnt = _desi_cnt.get(date=TruncDate(begin_date))['nums']
            date_entry.modi_files = _modi_files.get(date=TruncDate(begin_date))['nums']
            # 在每个日期中分别添加三个聚合字典中的对应值（核心贡献者）
            date_entry.comm_cnt_core = _comm_cnt_core.get(date=TruncDate(begin_date))['nums']
            date_entry.desi_cnt_core = _desi_cnt_core.get(date=TruncDate(begin_date))['nums']
            date_entry.modi_files_core = _modi_files_core.get(date=TruncDate(begin_date))['nums']
        except Exception:  # 缺少本日记录，计为0
            date_entry.comm_cnt = 0
            date_entry.desi_cnt = 0
            date_entry.modi_files = 0
            date_entry.comm_cnt_core = 0
            date_entry.desi_cnt_core = 0
            date_entry.modi_files_core = 0
        date_entry.modi_ins = '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
        date_entry.modi_del = '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
        # 对分小时的数据进行统计，统计增加和减少的行数
        #
        # # 删除的行数
        # del_set = pandas_commit_history.objects.annotate(date=TruncDate('commit_time')).filter(date=begin_date).annotate(
        # 	hour=ExtractHour('time_local')).values('hour').annotate(nums=Sum('modi_del'))
        # del_str = ""
        # for _h in range(24):
        # 	if _h is not 0:
        # 		del_str += ","
        # 	try:
        # 		stat = del_set.get(hour=str(_h))['nums']
        # 	except Exception:
        # 		stat = 0
        # 	del_str += str(stat)
        # date_entry.modi_del = del_str
        #
        # # 添加的行数
        # ins_set = pandas_commit_history.objects.annotate(date=TruncDate('commit_time')).filter(date=begin_date).annotate(
        # 	hour=ExtractHour('time_local')).values('hour').annotate(nums=Sum('modi_ins'))
        # ins_str = ""
        # for _h in range(24):
        # 	if _h is not 0:
        # 		ins_str += ","
        # 	try:
        # 		stat = ins_set.get(hour=str(_h))['nums']
        # 	except Exception:
        # 		stat = 0
        # 	ins_str += str(stat)
        # date_entry.modi_ins = ins_str

        # print(date_entry.date, date_entry.comm_cnt, date_entry.desi_cnt, date_entry.modi_files)

        # 保存对每一项的更改
        date_entry.save()
        begin_date += dt.timedelta(days=1)

    # 记录更新
    current_upd = pandas_commit_update()
    current_upd.time_update = datetime.now()
    current_upd.time_last_record = pandas_commit_history.objects.latest('commit_time').commit_time
    current_upd.save()
    return JsonResponse({'current_upd': current_upd.time_update})


def pandas_commit_update_byhour(_from: datetime):
    # 对齐到当日00:00:00
    last_upd = datetime(_from.year, _from.month, _from.day)

    # 遍历过程中的日期
    begin_date = last_upd
    end_date = datetime.now()

    while begin_date <= end_date:
        print(begin_date)
        try:
            date_entry = pandas_commit_by_day.objects.get(date=begin_date)
        except pandas_commit_by_day.DoesNotExist:
            date_entry = pandas_commit_by_day()
            date_entry.date = begin_date
            date_entry.modi_ins = '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'
            date_entry.modi_del = '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'

        # 对分小时的数据进行统计，统计增加和减少的行数

        # 删除的行数
        del_set = pandas_commit_history.objects.annotate(date=TruncDate('commit_time')).filter(
            date=begin_date).annotate(
            hour=ExtractHour('time_local')).values('hour').annotate(nums=Sum('modi_del'))
        del_str = ""
        for _h in range(24):
            if _h != 0:
                del_str += ","
            try:
                stat = del_set.get(hour=str(_h))['nums']
            except Exception:
                stat = 0
            del_str += str(stat)
        date_entry.modi_del = del_str

        # 添加的行数
        ins_set = pandas_commit_history.objects.annotate(date=TruncDate('commit_time')).filter(
            date=begin_date).annotate(
            hour=ExtractHour('time_local')).values('hour').annotate(nums=Sum('modi_ins'))
        ins_str = ""
        for _h in range(24):
            if _h != 0:
                ins_str += ","
            try:
                stat = ins_set.get(hour=str(_h))['nums']
            except Exception:
                stat = 0
            ins_str += str(stat)
        date_entry.modi_ins = ins_str

        # print(date_entry.date, date_entry.comm_cnt, date_entry.desi_cnt, date_entry.modi_files)

        # 保存对每一项的更改
        date_entry.save()
        begin_date += dt.timedelta(days=1)

    # 记录更新
    current_upd = pandas_commit_update()
    current_upd.time_update = datetime.now()
    current_upd.time_last_record = pandas_commit_history.objects.latest('commit_time').commit_time
    current_upd.save()


# 绘制设计讨论词云图，-> base64 str, utf-8
def graph_commit_intro_word_cloud(request):
    # 获取前端传回的起讫日期，传回词云图的base64字符串。
    # 时间格式为"%Y-%m-%d"
    time_start = datetime.strptime("2022-10-01", "%Y-%m-%d")
    time_end = datetime.strptime("2022-12-01", "%Y-%m-%d")
    # time_start = datetime.strptime(request.POST['start'], "%Y-%m-%d")
    # time_end = datetime.strptime(request.POST['end'], "%Y-%m-%d")
    intro_source = commit_history.objects.filter(commit_time__gte=time_start,
                                                 commit_time__lte=time_end,
                                                 if_design=True,
                                                 ).values('commit_intro')

    # 打开文本
    # os.chdir("/Users/ihsiao/Documents/SRE/pt_als")
    # with open("comments.txt", encoding="utf-8") as f:
    # 	s = f.read()

    # 生成输入字符串
    intro_buf = str(list(map(lambda x: x['commit_intro'], intro_source)))

    # # 生成对象
    img = Image.open("static/images/mask_cyy.jpeg")  # 打开遮罩图片
    mask = np.array(img)  # 将图片转换为数组

    stopwords = {"Fix", "Add", "Remove", "Use", "the", "py", "a", "in", "to", "for", "and", "of", "from", "with",
                 "on", "test", "tests", "support", "revert", "dynamo"}
    _wcloud = wordcloud.WordCloud(
        mask=mask,
        width=500,
        height=500,
        background_color=None,
        mode='RGBA',
        max_words=100,
        stopwords=stopwords,
        colormap="autumn")
    _wc = _wcloud.generate(intro_buf)

    # 生成png图片，储存在缓冲区中
    _buffer = io.BytesIO()
    _wc.to_image().save(_buffer, 'png')
    # 生成base64字符串，并传回前端
    _base64_str = base64.b64encode(_buffer.getvalue()).decode(encoding="utf-8")
    response = {'base64_png': _base64_str}
    # # 显示方法：<img src="data:image/png;base64,"+response['base64_png']/>
    # file_html = open("templates/render_base64.html", 'w', encoding='utf-8')
    # file_html.write('<img src="data:image/png;base64, ' + response['base64_png'] + '"/>')
    # file_html.close()
    # return render(request, "render_base64.html")
    return JsonResponse(response)


# 绘制设计讨论词云图，-> base64 str, utf-8
def pandas_graph_commit_intro_word_cloud(request):
    # 获取前端传回的起讫日期，传回词云图的base64字符串。
    # 时间格式为"%Y-%m-%d"
    time_start = datetime.strptime("2022-10-01", "%Y-%m-%d")
    time_end = datetime.strptime("2022-12-01", "%Y-%m-%d")
    # time_start = datetime.strptime(request.POST['start'], "%Y-%m-%d")
    # time_end = datetime.strptime(request.POST['end'], "%Y-%m-%d")
    intro_source = pandas_commit_history.objects.filter(commit_time__gte=time_start,
                                                        commit_time__lte=time_end,
                                                        if_design=True,
                                                        ).values('commit_intro')

    # 打开文本
    # os.chdir("/Users/ihsiao/Documents/SRE/pt_als")
    # with open("comments.txt", encoding="utf-8") as f:
    # 	s = f.read()

    # 生成输入字符串
    intro_buf = str(list(map(lambda x: x['commit_intro'], intro_source)))

    # # 生成对象
    img = Image.open("static/images/mask_cyy.jpeg")  # 打开遮罩图片
    mask = np.array(img)  # 将图片转换为数组

    stopwords = {"Fix", "Add", "Remove", "Use", "the", "py", "a", "in", "to", "for", "and", "of", "from", "with",
                 "on", "test", "tests", "support", "revert", "dynamo"}
    _wcloud = wordcloud.WordCloud(
        mask=mask,
        width=500,
        height=500,
        background_color=None,
        mode='RGBA',
        max_words=100,
        stopwords=stopwords,
        colormap="spring")
    _wc = _wcloud.generate(intro_buf)

    # 生成png图片，储存在缓冲区中
    _buffer = io.BytesIO()
    _wc.to_image().save(_buffer, 'png')
    # 生成base64字符串，并传回前端
    _base64_str = base64.b64encode(_buffer.getvalue()).decode(encoding="utf-8")
    response = {'base64_png': _base64_str}
    # # 显示方法：<img src="data:image/png;base64,"+response['base64_png']/>
    # file_html = open("templates/render_base64.html", 'w', encoding='utf-8')
    # file_html.write('<img src="data:image/png;base64, ' + response['base64_png'] + '"/>')
    # file_html.close()
    # return render(request, "render_base64.html")
    return JsonResponse(response)


# 绘制主要贡献者词云图 -> base64 str, utf-8
def pandas_graph_commit_contributor_word_cloud(request):
    primary_contributor = pandas_commit_contributors.objects.filter(if_core=True).values('author')
    # 生成输入字符串

    intro_buf = str(list(map(lambda x: x['author'], primary_contributor)))
    # intro_buf = ""
    # for i in primary_contributor:
    # 	intro_buf += i['author'] + " "
    # 生成对象
    img = Image.open("static/images/mask_cyy.jpeg")  # 打开遮罩图片
    mask = np.array(img)  # 将图片转换为数组

    _wcloud = wordcloud.WordCloud(
        mask=mask,
        width=500,
        height=500,
        background_color=None,
        mode='RGBA',
        max_words=100,
        colormap="summer")
    _wc = _wcloud.generate(intro_buf)
    _wc.to_file("data/pandas_contributor.png")  # 本地图片观察效果
    # 生成png图片，储存在缓冲区中
    _buffer = io.BytesIO()
    _wc.to_image().save(_buffer, 'png')
    # 生成base64字符串，并传回前端
    _base64_str = base64.b64encode(_buffer.getvalue()).decode(encoding="utf-8")
    response = {'base64_png': _base64_str}
    # # 显示方法：<img src="data:image/png;base64,"+response['base64_png']/>
    # file_html = open("templates/render_base64.html", 'w', encoding='utf-8')
    # file_html.write('<img src="data:image/png;base64, ' + response['base64_png'] + '"/>')
    # file_html.close()
    # return render(request, "render_base64.html")
    return JsonResponse(response)


# 绘制主要贡献者词云图 -> base64 str, utf-8
def graph_commit_contributor_word_cloud(request):
    primary_contributor = commit_contributors.objects.filter(if_core=True).values('author')
    # 生成输入字符串
    intro_buf = str(list(map(lambda x: x['author'], primary_contributor)))

    # # 生成对象
    img = Image.open("static/images/mask_cyy.jpeg")  # 打开遮罩图片
    mask = np.array(img)  # 将图片转换为数组

    _wcloud = wordcloud.WordCloud(
        mask=mask,
        width=500,
        height=500,
        background_color=None,
        mode='RGBA',
        max_words=100,
        colormap="winter")
    _wc = _wcloud.generate(intro_buf)

    # 生成png图片，储存在缓冲区中
    _buffer = io.BytesIO()
    _wc.to_image().save(_buffer, 'png')
    # 生成base64字符串，并传回前端
    _base64_str = base64.b64encode(_buffer.getvalue()).decode(encoding="utf-8")
    response = {'base64_png': _base64_str}
    # # 显示方法：<img src="data:image/png;base64,"+response['base64_png']/>
    # file_html = open("templates/render_base64.html", 'w', encoding='utf-8')
    # file_html.write('<img src="data:image/png;base64, ' + response['base64_png'] + '"/>')
    # file_html.close()
    # return render(request, "render_base64.html")
    return JsonResponse(response)


def pytorch_graph_issues_word_cloud(request):
    time_start = datetime.strptime("2022-10-01", "%Y-%m-%d")
    time_end = datetime.strptime("2022-12-21", "%Y-%m-%d")
    intro_source = pytorch_issues.objects.filter(updated_at__gte=time_start,
                                                 updated_at__lte=time_end,
                                                 ).values('title')
    # 生成输入字符串
    intro_buf = str(list(map(lambda x: x['title'], intro_source)))

    # # 生成对象
    img = Image.open("static/images/mask_cyy.jpeg")  # 打开遮罩图片
    mask = np.array(img)  # 将图片转换为数组

    stopwords = {"Fix", "Add", "Remove", "Use", "the", "py", "a", "in", "to", "for", "and", "of", "from", "with",
                 "on", "test", "tests", "support", "revert", "dynamo"}
    _wcloud = wordcloud.WordCloud(
        mask=mask,
        width=500,
        height=500,
        background_color=None,
        mode='RGBA',
        max_words=100,
        stopwords=stopwords,
        colormap="spring")
    _wc = _wcloud.generate(intro_buf)

    # 生成png图片，储存在缓冲区中
    _buffer = io.BytesIO()
    _wc.to_image().save(_buffer, 'png')
    # 生成base64字符串，并传回前端
    _base64_str = base64.b64encode(_buffer.getvalue()).decode(encoding="utf-8")
    response = {'base64_png': _base64_str}
    return JsonResponse(response)


def pandas_graph_issues_word_cloud(request):
    time_start = datetime.strptime("2022-10-01", "%Y-%m-%d")
    time_end = datetime.strptime("2022-12-21", "%Y-%m-%d")
    intro_source = pandas_issues.objects.filter(updated_at__gte=time_start,
                                                updated_at__lte=time_end,
                                                ).values('title')
    # 生成输入字符串
    intro_buf = str(list(map(lambda x: x['title'], intro_source)))

    # # 生成对象
    img = Image.open("static/images/mask_cyy.jpeg")  # 打开遮罩图片
    mask = np.array(img)  # 将图片转换为数组

    stopwords = {"Fix", "Add", "Remove", "Use", "the", "py", "a", "in", "to", "for", "and", "of", "from", "with",
                 "on", "test", "tests", "support", "revert", "dynamo"}
    _wcloud = wordcloud.WordCloud(
        mask=mask,
        width=500,
        height=500,
        background_color=None,
        mode='RGBA',
        max_words=100,
        stopwords=stopwords,
        colormap="spring")
    _wc = _wcloud.generate(intro_buf)

    # 生成png图片，储存在缓冲区中
    _buffer = io.BytesIO()
    _wc.to_image().save(_buffer, 'png')
    # 生成base64字符串，并传回前端
    _base64_str = base64.b64encode(_buffer.getvalue()).decode(encoding="utf-8")
    response = {'base64_png': _base64_str}
    return JsonResponse(response)


# 绘制每天分小时添加/删除行数的图
def graph_modi_time_of_day(request):
    # request: {'start':'日期，'end':'日期'}
    # response: {'x': [], 'add': [], 'del':[]}
    # 获取前端传回的起讫日期，传回词云图的base64字符串。
    # 时间格式为"%Y-%m-%d"
    time_start = datetime.strptime("2022-10-01", "%Y-%m-%d")
    time_end = datetime.strptime("2022-12-01", "%Y-%m-%d")
    # time_start = datetime.strptime(request.POST['start'], "%Y-%m-%d")
    # time_end = datetime.strptime(request.POST['end'], "%Y-%m-%d")
    stat_source = commit_by_day.objects.filter(date__gte=time_start,
                                               date__lte=time_end,
                                               ).values('modi_ins', 'modi_del')
    x_list = list(range(24))
    add_list = np.zeros(24)
    del_list = np.zeros(24)
    for entry in stat_source:
        try:
            add_list += list(map(lambda x: int(x, 10), entry['modi_ins'].split(',')))
            del_list += list(map(lambda x: int(x, 10), entry['modi_del'].split(',')))
        except Exception:
            continue
    add_list = list(map(lambda x: int(x), add_list))
    del_list = list(map(lambda x: int(x), del_list))
    response = {'x': x_list, 'add': add_list, 'del': del_list}
    return JsonResponse(response)


def pandas_graph_commit_intro_word_cloud(request):
    # 获取前端传回的起讫日期，传回词云图的base64字符串。
    # 时间格式为"%Y-%m-%d"
    time_start = datetime.strptime("2022-10-01", "%Y-%m-%d")
    time_end = datetime.strptime("2022-12-01", "%Y-%m-%d")
    # time_start = datetime.strptime(request.POST['start'], "%Y-%m-%d")
    # time_end = datetime.strptime(request.POST['end'], "%Y-%m-%d")
    intro_source = pandas_commit_history.objects.filter(commit_time__gte=time_start,
                                                        commit_time__lte=time_end,
                                                        if_design=True,
                                                        ).values('commit_intro')

    # 打开文本
    # os.chdir("/Users/ihsiao/Documents/SRE/pt_als")
    # with open("comments.txt", encoding="utf-8") as f:
    # 	s = f.read()

    # 生成输入字符串
    intro_buf = str(list(map(lambda x: x['commit_intro'], intro_source)))

    # # 生成对象
    img = Image.open("static/images/mask_cyy.jpeg")  # 打开遮罩图片
    mask = np.array(img)  # 将图片转换为数组

    stopwords = {"Fix", "Add", "Remove", "Use", "the", "py", "a", "in", "to", "for", "and", "of", "from", "with",
                 "on", "test", "tests", "support", "revert", "dynamo"}
    _wcloud = wordcloud.WordCloud(
        mask=mask,
        width=500,
        height=500,
        background_color=None,
        mode='RGBA',
        max_words=100,
        stopwords=stopwords,
        colormap="spring")
    _wc = _wcloud.generate(intro_buf)

    # 生成png图片，储存在缓冲区中
    _buffer = io.BytesIO()
    _wc.to_image().save(_buffer, 'png')
    # 生成base64字符串，并传回前端
    _base64_str = base64.b64encode(_buffer.getvalue()).decode(encoding="utf-8")
    response = {'base64_png': _base64_str}
    # # 显示方法：<img src="data:image/png;base64,"+response['base64_png']/>
    # file_html = open("templates/render_base64.html", 'w', encoding='utf-8')
    # file_html.write('<img src="data:image/png;base64, ' + response['base64_png'] + '"/>')
    # file_html.close()
    # return render(request, "render_base64.html")
    return JsonResponse(response)


def pandas_graph_modi_time_of_day(request):
    # request: {'start':'日期，'end':'日期'}
    # response: {'x': [], 'add': [], 'del':[]}
    # 获取前端传回的起讫日期，传回词云图的base64字符串。
    # 时间格式为"%Y-%m-%d"
    time_start = datetime.strptime("2022-11-01", "%Y-%m-%d")
    time_end = datetime.strptime("2022-12-01", "%Y-%m-%d")
    # time_start = datetime.strptime(request.POST['start'], "%Y-%m-%d")
    # time_end = datetime.strptime(request.POST['end'], "%Y-%m-%d")
    stat_source = pandas_commit_by_day.objects.filter(date__gte=time_start,
                                                      date__lte=time_end,
                                                      ).values('modi_ins', 'modi_del')
    x_list = list(range(24))
    add_list = np.zeros(24)
    del_list = np.zeros(24)
    for entry in stat_source:
        try:
            add_list += list(map(lambda x: int(x, 10), entry['modi_ins'].split(',')))
            del_list += list(map(lambda x: int(x, 10), entry['modi_del'].split(',')))
        except Exception:
            continue
    add_list = list(map(lambda x: int(x), add_list))
    del_list = list(map(lambda x: int(x), del_list))
    response = {'x': x_list, 'add': add_list, 'del': del_list}
    return JsonResponse(response)


# 比较两仓库提交情况
def comp_commit_by_week(request):
    # {'x':[,,,横坐标上的label],'pytorch_core':[,,每个label 对应的值,],'pytorch_else':[],'o_core':[],'o_else':[]}
    # 检查更新记录

    x_list = []
    pc_list = []
    pe_list = []
    oc_list = []
    oe_list = []

    try:
        # 选取两个仓库均有记录的日期开始比较
        time_start = max(commit_by_day.objects.earliest('date').date,
                         pandas_commit_by_day.objects.earliest('date').date)

        # pytorch
        db_src = commit_by_day.objects.filter(date__gte=time_start).annotate(week=TruncWeek('date')).values(
            'week').annotate(all=Sum('comm_cnt')).annotate(core=Sum('comm_cnt_core')).values('week', 'all', 'core')
        x_list = ['date'] + list(map(lambda x: x['week'].strftime("%Y-%m-%d"), db_src))
        pc_list = ['p_core'] + list(map(lambda x: x['core'], db_src))
        pe_list = ['p_else'] + list(map(lambda x: x['all'] - x['core'], db_src))

        # pandas
        pandas_db_src = pandas_commit_by_day.objects.filter(date__gte=time_start).annotate(
            week=TruncWeek('date')).values(
            'week').annotate(all=Sum('comm_cnt')).annotate(core=Sum('comm_cnt_core')).values('week', 'all', 'core')
        oc_list = ['o_core'] + list(map(lambda x: x['core'], pandas_db_src))
        oe_list = ['o_else'] + list(map(lambda x: x['all'] - x['core'], pandas_db_src))

    except commit_by_day.DoesNotExist or pandas_commit_by_day.DoesNotExist:
        # 不存在记录，无法画图
        pass
    return JsonResponse(
        {'x': x_list, 'pytorch_core': pc_list, 'pytorch_else': pe_list, 'o_core': oc_list, 'o_else': oe_list})


def comp_design_by_week(request):
    # {'x':[,,,横坐标上的label],'pytorch_core':[,,每个label 对应的值,],'pytorch_else':[],'o_core':[],'o_else':[]}

    x_list = []
    pc_list = []
    pe_list = []
    oc_list = []
    oe_list = []
    try:
        # 选取两个仓库均有记录的日期开始比较
        time_start = max(commit_by_day.objects.earliest('date').date,
                         pandas_commit_by_day.objects.earliest('date').date)

        # pytorch
        db_src = commit_by_day.objects.filter(date__gte=time_start).annotate(week=TruncWeek('date')).values(
            'week').annotate(all=Sum('desi_cnt')).annotate(core=Sum('desi_cnt_core')).values('week', 'all', 'core')
        x_list = ['date'] + list(map(lambda x: x['week'].strftime("%Y-%m-%d"), db_src))
        pc_list = ['p_core'] + list(map(lambda x: x['core'], db_src))
        pe_list = ['p_else'] + list(map(lambda x: x['all'] - x['core'], db_src))

        # pandas
        pandas_db_src = pandas_commit_by_day.objects.filter(date__gte=time_start).annotate(
            week=TruncWeek('date')).values(
            'week').annotate(all=Sum('desi_cnt')).annotate(core=Sum('desi_cnt_core')).values('week', 'all', 'core')
        oc_list = ['o_core'] + list(map(lambda x: x['core'], pandas_db_src))
        oe_list = ['o_else'] + list(map(lambda x: x['all'] - x['core'], pandas_db_src))
    except commit_by_day.DoesNotExist or pandas_commit_by_day.DoesNotExist:
        # 不存在记录，无法画图
        pass

    return JsonResponse(
        {'x': x_list, 'pytorch_core': pc_list, 'pytorch_else': pe_list, 'o_core': oc_list, 'o_else': oe_list})


def comp_file_by_week(request):
    # {'x':[,,,横坐标上的label],'pytorch_core':[,,每个label 对应的值,],'pytorch_else':[],'o_core':[],'o_else':[]}
    # 检查更新记录

    x_list = []
    pc_list = []
    pe_list = []
    oc_list = []
    oe_list = []

    try:
        # 选取两个仓库均有记录的日期开始比较
        time_start = max(commit_by_day.objects.earliest('date').date,
                         pandas_commit_by_day.objects.earliest('date').date)

        # pytorch
        db_src = commit_by_day.objects.filter(date__gte=time_start).annotate(week=TruncWeek('date')).values(
            'week').annotate(all=Sum('modi_files')).annotate(core=Sum('modi_files_core')).values('week', 'all', 'core')
        x_list = ['date'] + list(map(lambda x: x['week'].strftime("%Y-%m-%d"), db_src))
        pc_list = ['p_core'] + list(map(lambda x: x['core'], db_src))
        pe_list = ['p_else'] + list(map(lambda x: x['all'] - x['core'], db_src))

        # pandas
        pandas_db_src = pandas_commit_by_day.objects.filter(date__gte=time_start).annotate(
            week=TruncWeek('date')).values(
            'week').annotate(all=Sum('modi_files')).annotate(core=Sum('modi_files_core')).values('week', 'all', 'core')
        oc_list = ['o_core'] + list(map(lambda x: x['core'], pandas_db_src))
        oe_list = ['o_else'] + list(map(lambda x: x['all'] - x['core'], pandas_db_src))


    except commit_by_day.DoesNotExist or pandas_commit_by_day.DoesNotExist:
        # 不存在记录，无法画图
        pass
    return JsonResponse(
        {'x': x_list, 'pytorch_core': pc_list, 'pytorch_else': pe_list, 'o_core': oc_list, 'o_else': oe_list})


def comp_commit_by_week_brief(request):
    # {'x':[,,,横坐标上的label],'pytorch_core':[,,每个label 对应的值,],'pytorch_else':[],'o_core':[],'o_else':[]}
    # 检查更新记录

    x_list = []
    p_list = []
    o_list = []

    try:
        # 选取两个仓库均有记录的日期开始比较
        time_start = max(commit_by_day.objects.earliest('date').date,
                         pandas_commit_by_day.objects.earliest('date').date)

        # pytorch
        db_src = commit_by_day.objects.filter(date__gte=time_start).annotate(week=TruncWeek('date')).values(
            'week').annotate(all=Sum('comm_cnt')).values('week', 'all')
        x_list = ['date'] + list(map(lambda x: x['week'].strftime("%Y-%m-%d"), db_src))
        p_list = ['pytorch'] + list(map(lambda x: x['all'], db_src))

        # pandas
        pandas_db_src = pandas_commit_by_day.objects.filter(date__gte=time_start).annotate(
            week=TruncWeek('date')).values(
            'week').annotate(all=Sum('comm_cnt')).values('week', 'all')
        o_list = ['pandas'] + list(map(lambda x: x['all'], pandas_db_src))

    except commit_by_day.DoesNotExist or pandas_commit_by_day.DoesNotExist:
        # 不存在记录，无法画图
        pass
    return JsonResponse({'x': x_list, 'pytorch': p_list, 'pandas': o_list})


def comp_design_by_week_brief(request):
    # {'x':[,,,横坐标上的label],'pytorch_core':[,,每个label 对应的值,],'pytorch_else':[],'o_core':[],'o_else':[]}
    # 检查更新记录

    x_list = []
    p_list = []
    o_list = []

    try:
        # 选取两个仓库均有记录的日期开始比较
        time_start = max(commit_by_day.objects.earliest('date').date,
                         pandas_commit_by_day.objects.earliest('date').date)

        # pytorch
        db_src = commit_by_day.objects.filter(date__gte=time_start).annotate(week=TruncWeek('date')).values(
            'week').annotate(all=Sum('desi_cnt')).values('week', 'all')
        x_list = ['date'] + list(map(lambda x: x['week'].strftime("%Y-%m-%d"), db_src))
        p_list = ['pytorch'] + list(map(lambda x: x['all'], db_src))

        # pandas
        pandas_db_src = pandas_commit_by_day.objects.filter(date__gte=time_start).annotate(
            week=TruncWeek('date')).values(
            'week').annotate(all=Sum('desi_cnt')).values('week', 'all')
        o_list = ['pandas'] + list(map(lambda x: x['all'], pandas_db_src))

    except commit_by_day.DoesNotExist or pandas_commit_by_day.DoesNotExist:
        # 不存在记录，无法画图
        pass
    return JsonResponse({'x': x_list, 'pytorch': p_list, 'pandas': o_list})


def comp_file_by_week_brief(request):
    # {'x':[,,,横坐标上的label],'pytorch_core':[,,每个label 对应的值,],'pytorch_else':[],'o_core':[],'o_else':[]}
    # 检查更新记录

    x_list = []
    p_list = []
    o_list = []

    try:
        # 选取两个仓库均有记录的日期开始比较
        time_start = max(commit_by_day.objects.earliest('date').date,
                         pandas_commit_by_day.objects.earliest('date').date)

        # pytorch
        db_src = commit_by_day.objects.filter(date__gte=time_start).annotate(week=TruncWeek('date')).values(
            'week').annotate(all=Sum('modi_files')).values('week', 'all')
        x_list = ['date'] + list(map(lambda x: x['week'].strftime("%Y-%m-%d"), db_src))
        p_list = ['p_core'] + list(map(lambda x: x['all'], db_src))

        # pandas
        pandas_db_src = pandas_commit_by_day.objects.filter(date__gte=time_start).annotate(
            week=TruncWeek('date')).values(
            'week').annotate(all=Sum('modi_files')).values('week', 'all')
        o_list = ['o_core'] + list(map(lambda x: x['all'], pandas_db_src))

    except commit_by_day.DoesNotExist or pandas_commit_by_day.DoesNotExist:
        # 不存在记录，无法画图
        pass
    return JsonResponse({'x': x_list, 'pytorch': p_list, 'pandas': o_list})


# 绘制复合饼图
def compound_pie_chart_commit(request):
    # {'x': [,,, 横坐标上的label], 'core': [,, 每个label对应的值,], 'else':}
    db_src = commit_by_day.objects.annotate(week=TruncWeek('date')).values(
        'week').annotate(all=Sum('comm_cnt')).annotate(core=Sum('comm_cnt_core')).values('week', 'all', 'core')
    x_list = ['date'] + list(map(lambda x: x['week'].strftime("%Y-%m-%d"), db_src))
    core_list = ['core'] + list(map(lambda x: x['core'], db_src))
    else_list = ['else'] + list(map(lambda x: x['all'] - x['core'], db_src))
    return JsonResponse({'x': x_list, 'core': core_list, 'else': else_list})


def compound_pie_chart_design(request):
    # {'x': [,,, 横坐标上的label], 'core': [,, 每个label对应的值,], 'else':}
    db_src = commit_by_day.objects.annotate(week=TruncWeek('date')).values(
        'week').annotate(all=Sum('desi_cnt')).annotate(core=Sum('desi_cnt_core')).values('week', 'all', 'core')
    x_list = ['date'] + list(map(lambda x: x['week'].strftime("%Y-%m-%d"), db_src))
    core_list = ['core'] + list(map(lambda x: x['core'], db_src))
    else_list = ['else'] + list(map(lambda x: x['all'] - x['core'], db_src))
    return JsonResponse({'x': x_list, 'core': core_list, 'else': else_list})


def compound_pie_chart_file(request):
    # {'x': [,,, 横坐标上的label], 'core': [,, 每个label对应的值,], 'else':}
    db_src = commit_by_day.objects.annotate(week=TruncWeek('date')).values(
        'week').annotate(all=Sum('modi_files')).annotate(core=Sum('modi_files_core')).values('week', 'all', 'core')
    x_list = ['date'] + list(map(lambda x: x['week'].strftime("%Y-%m-%d"), db_src))
    core_list = ['core'] + list(map(lambda x: x['core'], db_src))
    else_list = ['else'] + list(map(lambda x: x['all'] - x['core'], db_src))
    return JsonResponse({'x': x_list, 'core': core_list, 'else': else_list})


# 绘制pandas的复合饼图
def pandas_compound_pie_chart_commit(request):
    # {'x': [,,, 横坐标上的label], 'core': [,, 每个label对应的值,], 'else':}
    db_src = pandas_commit_by_day.objects.annotate(week=TruncWeek('date')).values(
        'week').annotate(all=Sum('comm_cnt')).annotate(core=Sum('comm_cnt_core')).values('week', 'all', 'core')
    x_list = ['date'] + list(map(lambda x: x['week'].strftime("%Y-%m-%d"), db_src))
    core_list = ['core'] + list(map(lambda x: x['core'], db_src))
    else_list = ['else'] + list(map(lambda x: x['all'] - x['core'], db_src))
    return JsonResponse({'x': x_list, 'core': core_list, 'else': else_list})


def pandas_compound_pie_chart_design(request):
    # {'x': [,,, 横坐标上的label], 'core': [,, 每个label对应的值,], 'else':}
    db_src = pandas_commit_by_day.objects.annotate(week=TruncWeek('date')).values(
        'week').annotate(all=Sum('desi_cnt')).annotate(core=Sum('desi_cnt_core')).values('week', 'all', 'core')
    x_list = ['date'] + list(map(lambda x: x['week'].strftime("%Y-%m-%d"), db_src))
    core_list = ['core'] + list(map(lambda x: x['core'], db_src))
    else_list = ['else'] + list(map(lambda x: x['all'] - x['core'], db_src))
    return JsonResponse({'x': x_list, 'core': core_list, 'else': else_list})


def pandas_compound_pie_chart_file(request):
    # {'x': [,,, 横坐标上的label], 'core': [,, 每个label对应的值,], 'else':}
    db_src = pandas_commit_by_day.objects.annotate(week=TruncWeek('date')).values(
        'week').annotate(all=Sum('modi_files')).annotate(core=Sum('modi_files_core')).values('week', 'all', 'core')
    x_list = ['date'] + list(map(lambda x: x['week'].strftime("%Y-%m-%d"), db_src))
    core_list = ['core'] + list(map(lambda x: x['core'], db_src))
    else_list = ['else'] + list(map(lambda x: x['all'] - x['core'], db_src))
    return JsonResponse({'x': x_list, 'core': core_list, 'else': else_list})


def graph_design_by_week(request):
    db_src = commit_by_day.objects.annotate(
        week=TruncWeek('date')).values('week').annotate(nums=Sum('desi_cnt')).values('week', 'nums')
    x_list = ['date'] + list(map(lambda x: x['week'].strftime("%Y-%m-%d"), db_src))
    val_list = ['design'] + list(map(lambda x: x['nums'], db_src))
    return JsonResponse({'x': x_list, 'design': val_list})


def graph_file_by_week(request):
    db_src = commit_by_day.objects.annotate(
        week=TruncWeek('date')).values('week').annotate(nums=Sum('modi_files')).values('week', 'nums')
    x_list = ['date'] + list(map(lambda x: x['week'].strftime("%Y-%m-%d"), db_src))
    val_list = ['file'] + list(map(lambda x: x['nums'], db_src))
    return JsonResponse({'x': x_list, 'files': val_list})


def graph_commit_by_week(request):
    db_src = commit_by_day.objects.annotate(
        week=TruncWeek('date')).values('week').annotate(nums=Sum('comm_cnt')).values('week', 'nums')
    x_list = ['date'] + list(map(lambda x: x['week'].strftime("%Y-%m-%d"), db_src))
    val_list = ['commit'] + list(map(lambda x: x['nums'], db_src))
    return JsonResponse({'x': x_list, 'commit': val_list})


def pandas_graph_design_by_week(request):
    db_src = pandas_commit_by_day.objects.annotate(
        week=TruncWeek('date')).values('week').annotate(nums=Sum('desi_cnt')).values('week', 'nums')
    x_list = ['date'] + list(map(lambda x: x['week'].strftime("%Y-%m-%d"), db_src))
    val_list = ['design'] + list(map(lambda x: x['nums'], db_src))
    return JsonResponse({'x': x_list, 'design': val_list})


def pandas_graph_file_by_week(request):
    db_src = pandas_commit_by_day.objects.annotate(
        week=TruncWeek('date')).values('week').annotate(nums=Sum('modi_files')).values('week', 'nums')
    x_list = ['date'] + list(map(lambda x: x['week'].strftime("%Y-%m-%d"), db_src))
    val_list = ['file'] + list(map(lambda x: x['nums'], db_src))
    return JsonResponse({'x': x_list, 'files': val_list})


def pandas_graph_commit_by_week(request):
    db_src = pandas_commit_by_day.objects.annotate(
        week=TruncWeek('date')).values('week').annotate(nums=Sum('comm_cnt')).values('week', 'nums')
    x_list = ['date'] + list(map(lambda x: x['week'].strftime("%Y-%m-%d"), db_src))
    val_list = ['commit'] + list(map(lambda x: x['nums'], db_src))
    return JsonResponse({'x': x_list, 'commit': val_list})


def test(request):
    ############################
    # 初始化pytorch
    ############################

    # 使用data/_new.txt初始化数据库
    # 插入2022-12-25日以前的备份数据
    # git_log_to_file()
    commit_git_log_parser("data/_new.txt")

    # 取前10 % 的开发者为主要贡献者
    contributor_source = commit_contributors.objects.order_by('-modi_files')
    total_contributor = contributor_source.count()
    primary_contributor = contributor_source[:total_contributor / 10]
    for i in primary_contributor:
        i.if_core = True
        i.save()
    print("pytorch primary developers set!")

    # 更新by_day表的数据
    commit_update_main(request=request)

    # 计算2022-11-1之后的分小时提交详情
    commit_update_byhour(dt.datetime(2022, 10, 1))
    print("pytorch by_day set!")

    ############################
    # 初始化pandas
    ############################
    pandas_commit_git_log_parser("data/pandas_log.txt")
    print("pandas log read!")

    # 取前10 % 的开发者为主要贡献者
    contributor_source = pandas_commit_contributors.objects.order_by('-modi_files')
    total_contributor = contributor_source.count()
    primary_contributor = contributor_source[:total_contributor / 10]
    for i in primary_contributor:
        i.if_core = True
        i.save()
    print("pandas primary developers set!")

    # 更新by_day表的数据
    pandas_commit_update_main(request=request)

    # 计算2022-11-1之后的分小时提交详情
    pandas_commit_update_byhour(dt.datetime(2022, 10, 1))
    print("pandas by_day set!")
    return JsonResponse({'init': 'completed!'})
