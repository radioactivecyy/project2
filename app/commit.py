# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
import requests,json

def commit_from(request):

    contribute_datas = []
    type = '0'
    if request.POST:
        type = request.POST['s']
    if request.GET:
        result1 = []
        result2 = []
        result3 = []
        result4 = []
        target = request.GET['a']

        #获取commit数据
        url_contir = 'https://api.github.com/repos/' + target + '/commits'
        s = requests.session()
        s.keep_alive = False
        r = requests.get(url_contir)
        time_dict = {}
        committer_dict = {}
        total = 0
        resps = json.loads(r.content)
        for resps in resps:
            total = total + 1
            date_it = resps['commit']['author']['date']
            authors = resps['commit']['author']['name']
            if authors not in committer_dict.keys():
                committer_dict[resps['commit']['author']['name']] = 1

            else:
                committer_dict[resps['commit']['author']['name']] = committer_dict[resps['commit']['author']['name']] + 1
            date = list(date_it)
            date.pop(10)
            date.pop(18)
            l = ''
            l = l.join(date)
            dd = datetime.strptime(l, "%Y-%m-%d%H:%M:%S")
            dd = dd.date()
            contribute_datas.append(dd)
            contribute_datas = sorted(contribute_datas, reverse=False)


        #处理数据
        for date in contribute_datas:
            if type == '0':
                key = date.month + 0.01*date.day
            else :
                key = date.year +date.month * 0.01
            if key not in time_dict.keys():
                time_dict[key] = 1
            else:
                time_dict[key] = time_dict[key] + 1


        for name in time_dict.keys():
            re1 = name
            result1.append(re1)
            re2 = time_dict[name]
            result2.append(re2*100/total)

        for name in committer_dict.keys():
            re1 = name
            result3.append(re1)
            re2 = committer_dict[name]
            result4.append(re2)

    else:
        result1 = []
        result2 = []
        result3 = []
        result4 = []

    return render(request,'zhexian.html', {"target":target,"datas1": result1,"datas2":result2,"datas3":result3,"datas4":result4} )
