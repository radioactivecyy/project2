# 返回一个html页面
from django.shortcuts import render
from django.views.generic import View
from functools import cmp_to_key
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
import requests
from datetime import datetime
from .models import Contributors, Commits, date01, stargazer_company, stargazer_company_statistic, issue_company, \
    issue_company_statistic, committer_company, committer_company_statistic, total, pandas_stargazer_company, \
    pandas_stargazer_company_statistic, pandas_issue_company, pandas_issue_company_statistic, pandas_committer_company, \
    pandas_committer_company_statistic, pandas_total
import json
from django.http import JsonResponse
from github import Github
import datetime as dt
import github3
import re
import csv
import os

headers = {"Authorization": "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"}



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
    # cyy: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
    # jxx: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
    '''now_time = dt.datetime.now().strftime('%F %T')
    g = Github("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")  # 自己获取的github token
    repo = g.get_repo('pytorch/pytorch')  # 获取pytorch项目相关信息
    starcount = repo.stargazers_count
    j=0
    for i in range(400,int(starcount/100)+1):
        content_url = "https://api.github.com/repos/pytorch/pytorch/stargazers?page=" + str(i) + "&per_page=100"
        response = {}
        api_request = requests.get(content_url, headers=headers)
        contents = json.loads(api_request.content)
        print(type(contents))
        print(contents)
        for people in contents:
            j=j+1
            print(j)
            print(people)
            api_url=people["url"]
            reply=requests.get(api_url,headers=headers)
            info=json.loads(reply.content)
            if 'company'in info:
                if info['company']:
                    print(company_handle(info['company']))
                    stargazer_company.objects.create(node_id=info['node_id'], company=company_handle(info['company']),
                                                     get_time=now_time)'''
    # -------------------------------获取39990条数据
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
    '''response = {}
    for info in stargazer_company_statistic.objects.all():
        # print(info.company)
        # print(info.count)
        response[info.company] = info.count
        response['total'] = info.total
        response['update_time'] = info.update_time'''
    context = HttpResponse(content_type='text/csv')  # 告诉浏览器是text/csv格式
    context['Content-Disposition'] = 'attachment; filename="stargazer_company_statistic.csv"'  # csv文件名，不影响
    writer = csv.writer(context)
    writer.writerow(['company', 'count', 'total', 'update_time'])
    for info in stargazer_company_statistic.objects.all():
        writer.writerow([info.company, info.count, info.total, info.update_time])
    # return response
    print(context)
    return context
    # return JsonResponse(response)


def issue(request):
    # ------------------------------获取issue的assignee信息（可全部获取）
    '''
    # cyy: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
    # jxx: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
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
    '''response = {}
    for info in issue_company_statistic.objects.all():
        # print(info.company)
        # print(info.count)
        response[info.company] = info.count
        response['total'] = info.total
        response['update_time'] = info.update_time
    return JsonResponse(response)'''
    context = HttpResponse(content_type='text/csv')  # 告诉浏览器是text/csv格式
    context['Content-Disposition'] = 'attachment; filename="issue_company_statistic.csv"'  # csv文件名，不影响
    writer = csv.writer(context)
    writer.writerow(['company', 'count', 'total', 'update_time'])
    for info in issue_company_statistic.objects.all():
        writer.writerow([info.company, info.count, info.total, info.update_time])
    # return response
    print(context)
    return context


def committer(request):
    # cyy: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
    # jxx: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
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
    '''response = {}
    for info in committer_company_statistic.objects.all():
        # print(info.company)
        # print(info.count)
        response[info.company] = info.count
        response['total'] = info.total
        response['update_time'] = info.update_time
    return JsonResponse(response)'''
    context = HttpResponse(content_type='text/csv')  # 告诉浏览器是text/csv格式
    context['Content-Disposition'] = 'attachment; filename="committer_company_statistic.csv"'  # csv文件名，不影响
    writer = csv.writer(context)
    writer.writerow(['company', 'count', 'total', 'update_time'])
    for info in committer_company_statistic.objects.all():
        writer.writerow([info.company, info.count, info.total, info.update_time])
    # return response
    print(context)
    return context


def pr(request):
    response = {}
    pwd = os.system("cd pytorch/pytorch")

    print(pwd)
    return JsonResponse(response)


def update(request):
    response = {}
    g = Github("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")  # 自己获取的github token
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
    formal_total = stargazer_company_statistic.objects.get(company="Microsoft").total
    formal_total = count + formal_total
    formal = stargazer_company_statistic.objects.get(company="Microsoft").count
    stargazer_company_statistic.objects.filter(company="Microsoft").update(count=formal + microsoft_star,
                                                                           total=formal_total, update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="Google").count
    stargazer_company_statistic.objects.filter(company="Google").update(count=formal + google_star, total=formal_total,
                                                                        update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="Facebook").count
    stargazer_company_statistic.objects.filter(company="Facebook").update(count=formal + facebook_star,
                                                                          total=formal_total, update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="Alibaba").count
    stargazer_company_statistic.objects.filter(company="Alibaba").update(count=formal + alibaba_star,
                                                                         total=formal_total, update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="ByteDance").count
    stargazer_company_statistic.objects.filter(company="ByteDance").update(count=formal + bytedance_star,
                                                                           total=formal_total, update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="Tencent").count
    stargazer_company_statistic.objects.filter(company="Tencent").update(count=formal + tencent_star,
                                                                         total=formal_total, update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="TsinghuaUniversity").count
    stargazer_company_statistic.objects.filter(company="TsinghuaUniversity").update(count=formal + thu_star,
                                                                                    total=formal_total,
                                                                                    update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="PekingUniversity").count
    stargazer_company_statistic.objects.filter(company="PekingUniversity").update(count=formal + pku_star,
                                                                                  total=formal_total,
                                                                                  update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="Baidu").count
    stargazer_company_statistic.objects.filter(company="Baidu").update(count=formal + baidu_star,
                                                                       total=formal_total,
                                                                       update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="NVIDIA").count
    stargazer_company_statistic.objects.filter(company="NVIDIA").update(count=formal + nvidia_star,
                                                                        total=formal_total,
                                                                        update_time=now_time)
    formal = stargazer_company_statistic.objects.get(company="ZhejiangUniversity").count
    stargazer_company_statistic.objects.filter(company="ZhejiangUniversity").update(count=formal + zju_star,
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
        if i > issue_now - issue_formal: break
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
                                             company=company_handle(issue.assignee.company),
                                             get_time=now_time)
    formal_total = issue_company_statistic.objects.get(company="Microsoft").total
    formal_total = count + formal_total
    formal = issue_company_statistic.objects.get(company="Microsoft").count
    issue_company_statistic.objects.filter(company="Microsoft").update(count=formal + microsoft_issue,
                                                                       total=formal_total, update_time=now_time)
    formal = issue_company_statistic.objects.get(company="Quansight").count
    issue_company_statistic.objects.filter(company="Quansight").update(count=formal + quansight_issue,
                                                                       total=formal_total,
                                                                       update_time=now_time)
    formal = issue_company_statistic.objects.get(company="Facebook").count
    issue_company_statistic.objects.filter(company="Facebook").update(count=formal + facebook_issue,
                                                                      total=formal_total, update_time=now_time)
    formal = issue_company_statistic.objects.get(company="Pytorch").count
    issue_company_statistic.objects.filter(company="Pytorch").update(count=formal + pytorch_issue,
                                                                     total=formal_total, update_time=now_time)
    formal = issue_company_statistic.objects.get(company="Meta").count
    issue_company_statistic.objects.filter(company="Meta").update(count=formal + meta_issue,
                                                                  total=formal_total, update_time=now_time)
    formal = issue_company_statistic.objects.get(company="FacebookAI").count
    issue_company_statistic.objects.filter(company="FacebookAI").update(count=formal + facebookai_issue,
                                                                        total=formal_total, update_time=now_time)
    formal = issue_company_statistic.objects.get(company="GoogleLLC").count
    issue_company_statistic.objects.filter(company="GoogleLLC").update(count=formal + googlellc_issue,
                                                                       total=formal_total,
                                                                       update_time=now_time)
    formal = issue_company_statistic.objects.get(company="Intel").count
    issue_company_statistic.objects.filter(company="Intel").update(count=formal + intel_issue,
                                                                   total=formal_total,
                                                                   update_time=now_time)
    formal = issue_company_statistic.objects.get(company="NVIDIA").count
    issue_company_statistic.objects.filter(company="NVIDIA").update(count=formal + nvidia_issue,
                                                                    total=formal_total,
                                                                    update_time=now_time)
    formal = issue_company_statistic.objects.get(company="Hoofs&Horns,INC").count
    issue_company_statistic.objects.filter(company="Hoofs&Horns,INC").update(count=formal + hhinc_issue,
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
                                                     company=company_handle(commit.author.company),
                                                     get_time=now_time)
    formal_total = committer_company_statistic.objects.get(company="Facebook").total
    formal_total = count + formal_total
    formal = committer_company_statistic.objects.get(company="Alibaba,INC").count
    committer_company_statistic.objects.filter(company="Alibaba,INC").update(count=formal + alibabainc_committer,
                                                                             total=formal_total, update_time=now_time)
    formal = committer_company_statistic.objects.get(company="Quansight").count
    committer_company_statistic.objects.filter(company="Quansight").update(count=formal + quansight_committer,
                                                                           total=formal_total,
                                                                           update_time=now_time)
    formal = committer_company_statistic.objects.get(company="Facebook").count
    committer_company_statistic.objects.filter(company="Facebook").update(count=formal + facebook_committer,
                                                                          total=formal_total, update_time=now_time)
    formal = committer_company_statistic.objects.get(company="Pytorch").count
    committer_company_statistic.objects.filter(company="Pytorch").update(count=formal + pytorch_committer,
                                                                         total=formal_total, update_time=now_time)
    formal = committer_company_statistic.objects.get(company="Anduril").count
    committer_company_statistic.objects.filter(company="Anduril").update(count=formal + anduril_committer,
                                                                         total=formal_total, update_time=now_time)
    formal = committer_company_statistic.objects.get(company="FacebookAI").count
    committer_company_statistic.objects.filter(company="FacebookAI").update(count=formal + facebookai_committer,
                                                                            total=formal_total, update_time=now_time)
    formal = committer_company_statistic.objects.get(company="FacebookAIResearch").count
    committer_company_statistic.objects.filter(company="FacebookAIResearch").update(
        count=formal + facebookair_committer,
        total=formal_total, update_time=now_time)
    formal = committer_company_statistic.objects.get(company="Google").count
    committer_company_statistic.objects.filter(company="Google").update(count=formal + google_committer,
                                                                        total=formal_total,
                                                                        update_time=now_time)
    formal = committer_company_statistic.objects.get(company="Intel").count
    committer_company_statistic.objects.filter(company="Intel").update(count=formal + intel_committer,
                                                                       total=formal_total,
                                                                       update_time=now_time)
    formal = committer_company_statistic.objects.get(company="MIT CSAIL").count
    committer_company_statistic.objects.filter(company="MIT CSAIL").update(count=formal + mitcsail_committer,
                                                                           total=formal_total,
                                                                           update_time=now_time)
    formal = committer_company_statistic.objects.get(company="NVIDIA").count
    committer_company_statistic.objects.filter(company="NVIDIA").update(count=formal + nvidia_committer,
                                                                        total=formal_total,
                                                                        update_time=now_time)
    formal = committer_company_statistic.objects.get(company="ONNX").count
    committer_company_statistic.objects.filter(company="ONNX").update(count=formal + onnx_committer,
                                                                      total=formal_total,
                                                                      update_time=now_time)
    formal = committer_company_statistic.objects.get(company="Hoofs&Horns,INC").count
    committer_company_statistic.objects.filter(company="Hoofs&Horns,INC").update(count=formal + hhinc_committer,
                                                                                 total=formal_total,
                                                                                 update_time=now_time)
    # ---------------------------------------------------------------------------------------------------
    # total.objects.filter(source='stargazer').update(total=stargazer_now)
    total.objects.filter(source='issue').update(total=issue_now)
    total.objects.filter(source='committer').update(total=committer_now)
    return JsonResponse(response)


def pandas_star_gazer(request):
    # cyy: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
    # jxx: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
    # -------------------------------获取39990条数据
    '''g = Github("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")  # 自己获取的github token
    repo = g.get_repo('pandas-dev/pandas')  # 获取pandas项目相关信息
    starcount = repo.stargazers_count
    print(starcount)
    stargazers1 = repo.get_stargazers().reversed
    now_time = dt.datetime.now().strftime('%F %T')
    i = 0
    for people in stargazers1:
        i = i + 1
        print(i)
        if i > starcount-34574:
            break
        else:
            if people.company:
                print(company_handle(people.company))
                pandas_stargazer_company.objects.create(node_id=people.node_id, company=company_handle(people.company), get_time=now_time)'''
    # --------------------------------------------------------------
    context = HttpResponse(content_type='text/csv')  # 告诉浏览器是text/csv格式
    context['Content-Disposition'] = 'attachment; filename="pandas_stargazer_company_statistic.csv"'  # csv文件名，不影响
    writer = csv.writer(context)
    writer.writerow(['company', 'count', 'total', 'update_time'])
    for info in pandas_stargazer_company_statistic.objects.all():
        writer.writerow([info.company, info.count, info.total, info.update_time])
    # return response
    print(context)
    return context


def pandas_issue(request):
    # ------------------------------获取issue的assignee信息（可全部获取）
    # cyy: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
    # jxx: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
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
    context = HttpResponse(content_type='text/csv')  # 告诉浏览器是text/csv格式
    context['Content-Disposition'] = 'attachment; filename="pandas_issue_company_statistic.csv"'  # csv文件名，不影响
    writer = csv.writer(context)
    writer.writerow(['company', 'count', 'total', 'update_time'])
    for info in pandas_issue_company_statistic.objects.all():
        writer.writerow([info.company, info.count, info.total, info.update_time])
    # return response
    print(context)
    return context


def pandas_committer(request):
    # cyy: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
    # jxx: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
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
    context = HttpResponse(content_type='text/csv')  # 告诉浏览器是text/csv格式
    context['Content-Disposition'] = 'attachment; filename="pandas_committer_company_statistic.csv"'  # csv文件名，不影响
    writer = csv.writer(context)
    writer.writerow(['company', 'count', 'total', 'update_time'])
    for info in pandas_committer_company_statistic.objects.all():
        writer.writerow([info.company, info.count, info.total, info.update_time])
    # return response
    print(context)
    return context


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
        if i > stargazer_now - stargazer_formal: break
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
    formal_total = pandas_stargazer_company_statistic.objects.get(company="Amazon").total
    formal_total = count + formal_total
    formal = pandas_stargazer_company_statistic.objects.get(company="Amazon").count
    pandas_stargazer_company_statistic.objects.filter(company="Amazon").update(count=formal + amazon_star,
                                                                               total=formal_total, update_time=now_time)
    formal = pandas_stargazer_company_statistic.objects.get(company="Google").count
    pandas_stargazer_company_statistic.objects.filter(company="Google").update(count=formal + google_star,
                                                                               total=formal_total,
                                                                               update_time=now_time)
    formal = pandas_stargazer_company_statistic.objects.get(company="Facebook").count
    pandas_stargazer_company_statistic.objects.filter(company="Facebook").update(count=formal + facebook_star,
                                                                                 total=formal_total,
                                                                                 update_time=now_time)
    formal = pandas_stargazer_company_statistic.objects.get(company="Alibaba").count
    pandas_stargazer_company_statistic.objects.filter(company="Alibaba").update(count=formal + alibaba_star,
                                                                                total=formal_total,
                                                                                update_time=now_time)
    formal = pandas_stargazer_company_statistic.objects.get(company="ByteDance").count
    pandas_stargazer_company_statistic.objects.filter(company="ByteDance").update(count=formal + bytedance_star,
                                                                                  total=formal_total,
                                                                                  update_time=now_time)
    formal = pandas_stargazer_company_statistic.objects.get(company="Tencent").count
    pandas_stargazer_company_statistic.objects.filter(company="Tencent").update(count=formal + tencent_star,
                                                                                total=formal_total,
                                                                                update_time=now_time)
    formal = pandas_stargazer_company_statistic.objects.get(company="IBM").count
    pandas_stargazer_company_statistic.objects.filter(company="IBM").update(count=formal + ibm_star,
                                                                            total=formal_total,
                                                                            update_time=now_time)
    formal = pandas_stargazer_company_statistic.objects.get(company="PekingUniversity").count
    pandas_stargazer_company_statistic.objects.filter(company="PekingUniversity").update(count=formal + pku_star,
                                                                                         total=formal_total,
                                                                                         update_time=now_time)
    formal = pandas_stargazer_company_statistic.objects.get(company="Baidu").count
    pandas_stargazer_company_statistic.objects.filter(company="Baidu").update(count=formal + baidu_star,
                                                                              total=formal_total,
                                                                              update_time=now_time)
    formal = pandas_stargazer_company_statistic.objects.get(company="Intel").count
    pandas_stargazer_company_statistic.objects.filter(company="Intel").update(count=formal + intel_star,
                                                                              total=formal_total,
                                                                              update_time=now_time)
    formal = pandas_stargazer_company_statistic.objects.get(company="Meta").count
    pandas_stargazer_company_statistic.objects.filter(company="Meta").update(count=formal + meta_star,
                                                                             total=formal_total,
                                                                             update_time=now_time)
    formal = pandas_stargazer_company_statistic.objects.get(company="Nubank").count
    pandas_stargazer_company_statistic.objects.filter(company="Nubank").update(count=formal + nubank_star,
                                                                               total=formal_total,
                                                                               update_time=now_time)
    formal = pandas_stargazer_company_statistic.objects.get(company="VMware").count
    pandas_stargazer_company_statistic.objects.filter(company="VMware").update(count=formal + vm_star,
                                                                               total=formal_total,
                                                                               update_time=now_time)
    formal = pandas_stargazer_company_statistic.objects.get(company="ZhejiangUniversity").count
    pandas_stargazer_company_statistic.objects.filter(company="ZhejiangUniversity").update(count=formal + zju_star,
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
        if i > issue_now - issue_formal: break
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
                                                    company=company_handle(issue.assignee.company),
                                                    get_time=now_time)
    formal_total = pandas_issue_company_statistic.objects.get(company="Farfetch").total
    formal_total = count + formal_total
    formal = pandas_issue_company_statistic.objects.get(company="84.51°").count
    pandas_issue_company_statistic.objects.filter(company="84.51°").update(count=formal + c8451_issue,
                                                                           total=formal_total, update_time=now_time)
    formal = pandas_issue_company_statistic.objects.get(company="Factored AI").count
    pandas_issue_company_statistic.objects.filter(company="Factored AI").update(count=formal + factor_issue,
                                                                                total=formal_total,
                                                                                update_time=now_time)
    formal = pandas_issue_company_statistic.objects.get(company="Farfetch").count
    pandas_issue_company_statistic.objects.filter(company="Farfetch").update(count=formal + farfetch_issue,
                                                                             total=formal_total, update_time=now_time)
    formal = pandas_issue_company_statistic.objects.get(company="PandasDev").count
    pandas_issue_company_statistic.objects.filter(company="PandasDev").update(count=formal + pandas_issue1,
                                                                              total=formal_total, update_time=now_time)
    formal = pandas_issue_company_statistic.objects.get(company="Voltron Data").count
    pandas_issue_company_statistic.objects.filter(company="Voltron Data").update(count=formal + vol_issue,
                                                                                 total=formal_total,
                                                                                 update_time=now_time)
    formal = pandas_issue_company_statistic.objects.get(company="Zonos").count
    pandas_issue_company_statistic.objects.filter(company="Zonos").update(count=formal + zonos_issue,
                                                                          total=formal_total, update_time=now_time)
    formal = pandas_issue_company_statistic.objects.get(company="Zyppio").count
    pandas_issue_company_statistic.objects.filter(company="Zyppio").update(count=formal + zyppio_issue,
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
                                                            company=company_handle(commit.author.company),
                                                            get_time=now_time)
    formal_total = pandas_committer_company_statistic.objects.get(company="DLR").total
    formal_total = count + formal_total
    formal = pandas_committer_company_statistic.objects.get(company="84.51°").count
    pandas_committer_company_statistic.objects.filter(company="84.51°").update(count=formal + c8451_committer,
                                                                               total=formal_total, update_time=now_time)
    formal = pandas_committer_company_statistic.objects.get(company="Quansight").count
    pandas_committer_company_statistic.objects.filter(company="Quansight").update(count=formal + quansight_committer,
                                                                                  total=formal_total,
                                                                                  update_time=now_time)
    formal = pandas_committer_company_statistic.objects.get(company="DLR").count
    pandas_committer_company_statistic.objects.filter(company="DLR").update(count=formal + dlr_committer,
                                                                            total=formal_total, update_time=now_time)
    formal = pandas_committer_company_statistic.objects.get(company="HCA Healthcare").count
    pandas_committer_company_statistic.objects.filter(company="HCA Healthcare").update(count=formal + hca_committer,
                                                                                       total=formal_total,
                                                                                       update_time=now_time)
    formal = pandas_committer_company_statistic.objects.get(company="Innobi").count
    pandas_committer_company_statistic.objects.filter(company="Innobi").update(count=formal + innobi_committer,
                                                                               total=formal_total, update_time=now_time)
    formal = pandas_committer_company_statistic.objects.get(company="Microsoft").count
    pandas_committer_company_statistic.objects.filter(company="Microsoft").update(count=formal + microsoft_committer,
                                                                                  total=formal_total,
                                                                                  update_time=now_time)
    formal = pandas_committer_company_statistic.objects.get(company="Palantir Technologies").count
    pandas_committer_company_statistic.objects.filter(company="Palantir Technologies").update(
        count=formal + palantir_committer,
        total=formal_total, update_time=now_time)
    formal = pandas_committer_company_statistic.objects.get(company="Google").count
    pandas_committer_company_statistic.objects.filter(company="Google").update(count=formal + google_committer,
                                                                               total=formal_total,
                                                                               update_time=now_time)
    formal = pandas_committer_company_statistic.objects.get(company="Pythomation").count
    pandas_committer_company_statistic.objects.filter(company="Pythomation").update(count=formal + pytho_committer,
                                                                                    total=formal_total,
                                                                                    update_time=now_time)
    formal = pandas_committer_company_statistic.objects.get(company="RAPIDS AI").count
    pandas_committer_company_statistic.objects.filter(company="RAPIDS AI").update(count=formal + rapids_committer,
                                                                                  total=formal_total,
                                                                                  update_time=now_time)
    formal = pandas_committer_company_statistic.objects.get(company="Tubi TV").count
    pandas_committer_company_statistic.objects.filter(company="Tubi TV").update(count=formal + tubi_committer,
                                                                                total=formal_total,
                                                                                update_time=now_time)
    formal = pandas_committer_company_statistic.objects.get(company="Voltron Data").count
    pandas_committer_company_statistic.objects.filter(company="Voltron Data").update(count=formal + vol_committer,
                                                                                     total=formal_total,
                                                                                     update_time=now_time)
    formal = pandas_committer_company_statistic.objects.get(company="PandasDev").count
    pandas_committer_company_statistic.objects.filter(company="PandasDev").update(count=formal + pandas_committer1,
                                                                                  total=formal_total,
                                                                                  update_time=now_time)
    formal = pandas_committer_company_statistic.objects.get(company="WashingtonUniversityinStLouis").count
    pandas_committer_company_statistic.objects.filter(company="WashingtonUniversityinStLouis").update(
        count=formal + was_committer,
        total=formal_total,
        update_time=now_time)
    # ---------------------------------------------------------------------------------------------------
    pandas_total.objects.filter(source='stargazer').update(total=stargazer_now)
    pandas_total.objects.filter(source='issue').update(total=issue_now)
    pandas_total.objects.filter(source='committer').update(total=committer_now)
    return JsonResponse(response)


def real_index(request):
    response = {}
    panduan = date01.objects.filter(repo_name='2021-sr-bighw')  # 判断本地有没有记录
    if panduan.exists():  # 如果有就把时间打印出来
        # time01 = date01.date_lasttime  #没有成功获取到一条数据
        response['time01'] = '2022-10-18 22:22:22'
        return JsonResponse(response)
    response['time01'] = 'null'  # 没有获取到时间，time01值为null
    return JsonResponse(response)


def about_us(request):
    commit_users = []
    commit_users.append({"name": "张济开", "user": "Zhangjk2000", "url": "https://github.com/Zhangjk2000",
                        "a_url": "https://avatars.githubusercontent.com/u/85881886?v=4"})
    commit_users.append({"name": "温相龙", "user": "wwwxxxxlll", "url": "https://github.com/wwwxxxxlll",
                        "a_url": "https://avatars.githubusercontent.com/u/84766861?v=4"})
    commit_users.append({"name": "罗云", "user": "12321231", "url": "https://github.com/12321231",
                        "a_url": "https://avatars.githubusercontent.com/u/52814667?v=4"})
    commit_users.append({"name": "曲浩天", "user": "quhaotia", "url": "https://github.com/quhaotia",
                        "a_url": "https://avatars.githubusercontent.com/u/91251905?v=4"})
    commit_users.append({"name": "董博", "user": "shenkongshiyi", "url": "https://github.com/shenkongshiyi",
                        "a_url": "https://avatars.githubusercontent.com/u/81542105?v=4"})
    commit_users.append({"name": "陈奕宇", "user": "radioactivecyy", "url": "https://github.com/radioactivecyy",
                         "a_url": "https://avatars.githubusercontent.com/u/81542105?v=4"})
    # return JsonResponse(commit_users)
    return render(request, 'about-us.html', {"us": commit_users})


def notfound(request):
    return render(request, '404.html')


def intro(request):
    return render(request, '说明.html')


def index(request):
    return render(request, 'brief_info.html', {})
# 设置主页对应的页面 + 传到主页的数据内容


def commit(request):
    if request.method == 'POST':
        url = request.POST['url']
        print(url)
        u_list = url.strip().split('/')
        api_url = 'https://api.github.com/repos/' + \
            u_list[3]+'/'+u_list[4]+'/commits'
        print(api_url)
        content_url = 'https://api.github.com/repos/' + u_list[3] + '/' + u_list[4]
        api_request = requests.get(content_url, headers=headers)
        contents = json.loads(api_request.content)
        print(contents)
        if contents:
            owner = contents['owner']['login']
            print(owner)
            avatar_url = contents['owner']['avatar_url']
            html_url = contents['owner']['html_url']
            description = contents['description']
            topics = contents['topics']
            stargazers_count = contents['stargazers_count']
            created_at = contents['created_at']
            id = contents['id']
            api_request = requests.get(api_url)
            api_ret = json.loads(api_request.content)
            print("\n")
            print(api_ret)
            committer_dict = {}
            date_list = []
            for committer in api_ret:
                date_it = committer['commit']['author']['date']
                print(date_it)
                date = list(date_it)
                date.pop(10)
                date.pop(18)
                l = ''
                l = l.join(date)
                dd = datetime.strptime(l, "%Y-%m-%d%H:%M:%S")
                print(dd)
                date_list.append(dd)

                # 数据插入数据库,commits的数据
                dbdic = {'o_name': u_list[3], 'r_name': u_list[4],
                         'c_name': committer['commit']['author']['name']}
                Commits.objects.create(
                    owner_name=dbdic['o_name'], repo_name=dbdic['r_name'], con_name=dbdic['c_name'])
                # 获取并插入时间，对字符串处理一下存进数据库
                date1 = committer['commit']['author']['date'][0:10] + \
                    ' ' + committer['commit']['author']['date'][11:19]
                date01.objects.create(
                    repo_name=dbdic['r_name'], date_newest=date1, date_lasttime=date1)

            sorted_date = sorted(date_list, reverse=True)
            print(sorted_date)
            date_newest = sorted_date[0]
            print(date_newest)
            # 插入数据库date_newest与u_list[3],u_list[4]
            for committer in api_ret:
                if "author" in committer.keys():
                    if "login" in committer.keys():
                        if committer['author']['login'] not in committer_dict.keys():
                            committer_dict[committer['author']['login']] = 1
                        else:
                            committer_dict[committer['author']['login']] = committer_dict[
                                                                               committer['author']['login']] + 1
            print(committer_dict)
            sorted_dict = {}
            sorted_dict = sorted(committer_dict.items(),
                                 key=lambda kv: (kv[1], kv[0]), reverse=True)
            print(sorted_dict)
            target = u_list[3] + '/' + u_list[4]

            # print(sorted_dict)
            commit_users = []
            for test in sorted_dict:
                commit_url = 'https://github.com/' + test[0]
                print('https://api.github.com/users/' + test[0])
                print(commit_url)
                api_request = requests.get(
                    'https://api.github.com/users/' + test[0], headers=headers)
                user_info = json.loads(api_request.content)
                avatar_url_1 = user_info['avatar_url']
                commit_users.append(
                    {"user": test[0], "url": commit_url, "a_url": avatar_url_1})
            # for i in range(0,3):
            #     if sorted_dict[i]:
            #         commit_url = 'https://github.com/'+sorted_dict[i][0]
            #         api_request = requests.get('https://api.github.com/users/'+sorted_dict[i][0], headers=headers)
            #         user_info = json.loads(api_request.content)
            #         avatar_url_1 = user_info['avatar_url']
            #         commit_users.append({"user":sorted_dict[i][0],"url":commit_url,"a_url":avatar_url_1})
            #
            return render(request, 'brief_info.html', {"target": target, "id": id, "url": url, "owner": owner, "avatar_url": avatar_url, "html_url": html_url, "description": description, "topics": topics, "stargazers_count": stargazers_count, "created_at": created_at, "commit_users": commit_users, "date_newest": date_newest})


def user(request):
    # 获取搜索框中输入的内容，前端搜索框文本的名称为input_content
    user_name = request.POST['input_content']
    if user_name:  # 输入内容不为空
        # 同home函数中获取api接口内容
        user_request = requests.get(
            url='https://api.github.com/users/' + user_name)
        user_info = json.loads(user_request.content)
        # 返回函数包含两个数据，分别是要搜索的用户名和对应的用户信息
        response = {'input_contents': user_name, 'user_info': user_info}
        return JsonResponse(response)
        # return render(request, 'user.html', {'input_contents': user_name, 'user_info': user_info})
    else:
        # 若搜索框内没有输入，则进行提示
        notfound = '请在搜索框中输入您需要查询的用户...'
        response = {'notfound': notfound}
        return JsonResponse(response)
        # return render(request, 'user.html', {'notfound': notfound})

# class Contribution(View):
#    def get(self,request):
#        contribute_data = []
#        conact = {}
#        if request.POST:
#            conact = request.POST.get('urn')
#            print(conact)
#            print("1")
#            contribute_data = {'value': 0, 'name': '0'}
#        else:
#            contribute_data = {'value': 0, 'name': ''}
#        return render(request,'contribution.html', {"contribute_data": contribute_data} )
