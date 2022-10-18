# -*- coding: utf-8 -*-
from django.shortcuts import render
import requests
from django.http import JsonResponse

def Contribution_from(request):
    contribute_datas = []
    if request.GET:
        url = request.GET['a']
        url_contir = 'https://api.github.com/repos/' + url +'/contributors'
        print(url_contir)
        s = requests.session()
        s.keep_alive = False
        r = requests.get(url_contir)
        resps = r.json()
        for resps in resps:
            contribute_data = {
                'value':resps['contributions'],
                'name':resps['login']
            }
            contribute_datas.append(contribute_data)
    else:
        contribute_datas = []
    response={}
    response['contribute_datas']=contribute_datas
    return JsonResponse(response)
    #return render(request,'contribution.html', {"contribute_datas": contribute_datas} )