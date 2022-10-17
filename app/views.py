#返回一个html页面
from django.shortcuts import render
from django.views.generic import View
from functools import cmp_to_key
from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from datetime import datetime
from .models import Contributors,Commits,date01
import json
headers = {"Authorization": "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"}

# Create your views here.
def real_index(request):
    panduan = date01.objects.filter(repo_name='2021-sr-bighw')#判断本地有没有记录
    if panduan.exists():#如果有就把时间打印出来
        # time01 = date01.date_lasttime  #没有成功获取到一条数据
        return render(request,'home.html',{'time01':'2021-12-20 06:32:20'})#时间传回首页
    return render(request,'home.html')
def about_us(request):
    commit_users = []
    commit_users.append({"name":"张济开","user":"Zhangjk2000","url":"https://github.com/Zhangjk2000","a_url":"https://avatars.githubusercontent.com/u/85881886?v=4"})
    commit_users.append({"name":"温相龙","user":"wwwxxxxlll","url":"https://github.com/wwwxxxxlll","a_url":"https://avatars.githubusercontent.com/u/84766861?v=4"})
    commit_users.append({"name":"罗云","user":"12321231","url":"https://github.com/12321231","a_url":"https://avatars.githubusercontent.com/u/52814667?v=4"})
    commit_users.append({"name":"曲浩天","user":"quhaotia","url":"https://github.com/quhaotia","a_url": "https://avatars.githubusercontent.com/u/91251905?v=4"})
    commit_users.append({"name":"董博","user":"shenkongshiyi","url":"https://github.com/shenkongshiyi","a_url":"https://avatars.githubusercontent.com/u/81542105?v=4"})
    commit_users.append({"name": "陈奕宇", "user": "radioactivecyy", "url": "https://github.com/radioactivecyy",
                         "a_url": "https://avatars.githubusercontent.com/u/81542105?v=4"})

    return render(request,'about-us.html',{"us":commit_users})
def notfound(request):
    return render(request,'404.html')
def intro(request):
    return render(request,'说明.html')
def index(request):
    return render(request,'brief_info.html',{})
# 设置主页对应的页面 + 传到主页的数据内容



def commit(request):
    if request.method == 'POST':
        url = request.POST['url']
        print(url)
        u_list = url.strip().split('/')
        api_url = 'https://api.github.com/repos/'+u_list[3]+'/'+u_list[4]+'/commits'
        print(api_url)
        content_url = 'https://api.github.com/repos/'+u_list[3]+'/'+u_list[4]
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
            created_at =  contents['created_at']
            id = contents['id']
            api_request = requests.get(api_url)
            api_ret = json.loads(api_request.content)
            print("\n")
            print(api_ret)
            committer_dict = {}
            date_list = []
            for committer in api_ret:    
                date_it = committer['commit']['author']['date']
                date = list(date_it)
                date.pop(10)
                date.pop(18)
                l = ''
                l = l.join(date)
                dd = datetime.strptime(l, "%Y-%m-%d%H:%M:%S")
                print(dd)
                date_list.append(dd)

                # 数据插入数据库,commits的数据
                dbdic = {'o_name': u_list[3], 'r_name': u_list[4], 'c_name': committer['commit']['author']['name']}
                Commits.objects.create(owner_name = dbdic['o_name'],repo_name=dbdic['r_name'],con_name=dbdic['c_name'])
                # 获取并插入时间，对字符串处理一下存进数据库
                date1 = committer['commit']['author']['date'][0:10] + ' ' + committer['commit']['author']['date'][11:19]
                date01.objects.create(repo_name=dbdic['r_name'],date_newest = date1,date_lasttime = date1)

            sorted_date = sorted(date_list,reverse=True)
            print(sorted_date)
            date_newest = sorted_date[0]
            print(date_newest)
            #插入数据库date_newest与u_list[3],u_list[4]
            for committer in api_ret:
                if "author" in committer.keys():
                    if "login" in committer.keys():
                        if committer['author']['login']not in committer_dict.keys():
                            committer_dict[committer['author']['login']] = 1
                        else:
                            committer_dict[committer['author']['login']] = committer_dict[committer['author']['login']] + 1
            print(committer_dict)
            sorted_dict = {}
            sorted_dict = sorted(committer_dict.items(), key = lambda kv:(kv[1], kv[0]),reverse = True)
            print(sorted_dict)
            target = u_list[3]+'/'+u_list[4]


            #print(sorted_dict)
            commit_users = []
            for test in sorted_dict:
                commit_url = 'https://github.com/' + test[0]
                print('https://api.github.com/users/' +test[0])
                print(commit_url)
                api_request = requests.get('https://api.github.com/users/' + test[0], headers=headers)
                user_info = json.loads(api_request.content)
                avatar_url_1 = user_info['avatar_url']
                commit_users.append({"user": test[0], "url": commit_url, "a_url": avatar_url_1})
            # for i in range(0,3):
            #     if sorted_dict[i]:
            #         commit_url = 'https://github.com/'+sorted_dict[i][0]
            #         api_request = requests.get('https://api.github.com/users/'+sorted_dict[i][0], headers=headers)
            #         user_info = json.loads(api_request.content)
            #         avatar_url_1 = user_info['avatar_url']
            #         commit_users.append({"user":sorted_dict[i][0],"url":commit_url,"a_url":avatar_url_1})
            #
            return render(request,'brief_info.html',{"target":target,"id":id,"url":url,"owner":owner,"avatar_url":avatar_url,"html_url":html_url,"description":description,"topics":topics,"stargazers_count":stargazers_count,"created_at":created_at,"commit_users":commit_users,"date_newest":date_newest})

def user(request):
    # 获取搜索框中输入的内容，前端搜索框文本的名称为input_content
    user_name = request.POST['input_content']
    if user_name:  # 输入内容不为空
        # 同home函数中获取api接口内容
        user_request = requests.get(url='https://api.github.com/users/' + user_name)
        user_info = json.loads(user_request.content)
        # 返回函数包含两个数据，分别是要搜索的用户名和对应的用户信息
        return render(request, 'user.html', {'input_contents': user_name, 'user_info': user_info})
    else:
        # 若搜索框内没有输入，则进行提示
        notfound = '请在搜索框中输入您需要查询的用户...'
        return render(request, 'user.html', {'notfound': notfound})

#class Contribution(View):
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