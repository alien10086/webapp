# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from editor.models import  Author, Entry
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.models import User





def index(request):
    article_list = Entry.objects.order_by('-pub_date')[:10]
    context = {'article_list': article_list}
    return render(request, 'editor/index.html',context)

def login(request):
    return render(request, 'login/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'login/login.html')



def add_register(request):
    if request.method == 'GET':
        return render(request, 'editor/register.html')




def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['e-mail']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        try:
           filterResult = User.objects.filter(username = username)
           if len(filterResult)>0:

               context = {'errors': "账户已存在"}
               #return HttpResponse("用户名已存在")
               # csrf 要求 改变字典的格式，由普通字典变为RequestContext
               return render(request, 'editor/register.html',context)
           elif password != password1:

               context = {'errors': "两次输入的密码不一致!"}

               return render(request, 'editor/register.html', context)
#return HttpResponse('两次输入的密码不一致!,请重新输入密码')
           else:
#将表单写入数据库,使用django默认的user
                user = User.objects.create_user(username,email,password)
                user.last_name = lastname
                user.first_name = firstname

                user.save()
                context = {'username':username,'operation':"注册"}

#返回注册成功页面
                return render(request, 'login/login.html', context)
        except Exception as e:


            return HttpResponse(e)






def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username = username, password = password)
    if user is not None:
#官方文档有错误，需要使用auth.login而不是，login（）
        auth.login(request, user)
        context = {'username':user.username, 'operation' :'登陆'}
        return render(request,'editor/succeed.html', context)


    else:
        return HttpResponse("账户不存在")


@login_required(login_url='editor/login')
def homepage(request):
    username =request.user.username
    article_list = Entry.objects.filter(author__name= username).order_by('-pub_date')
    context = {'article_list': article_list, 'username':username}
    return render(request, 'editor/homepage.html',context)








@login_required(login_url='editor/login')
def add_article(request):
    return render(request, 'editor/makedown/widget.html')


def have(name1):
    try:
        a = Author.objects.get(name=name1)
        return True
    except :
        b = Author(name=name1)
        b.save()
        return True

def sub_article(request):
    if request.method == 'GET':
        name1 = request.user.username
        title1 = request.GET['headline']
        body = request.GET['body_text']
        have(name1)
        b = Author.objects.get(name=name1)

        updb = Entry(author = b,
         headline = title1,
         body_text = body,
         pub_date = timezone.now())
        updb.save()
        entry_id = updb.id
        contex ={'headline':title1, 'body_text':body, 'entry_id':entry_id}
        return render(request,'editor/look.html',context)

def compile(request, article_id):
    one_entry = Entry.objects.get(pk=article_id)
    headline =one_entry.headline
    body_text =one_entry.headline
    context ={'headline':headline, 'body_text':body_text,
    'one_entry':one_entry}
    return render(request, 'editor/makedown/widget.html',context)

def edit(request ,article_id):
    if request.method == 'GET':
        one_entry = Entry.objects.get(pk=article_id)
        title1 = request.GET['headline']
        body = request.GET['body_text']
        one_entry.headline = title1
        one_entry.body_text =body
        one_entry.save()

        context = {'headline':title1,'body_text':body,'entry':one_entry}
        return render(request,'editor/look.html',context )








#entry_id来自 homepage模版的 m.id  (urlcon捕获它并赋值给entry_id ，然后传导过来。）
def look(request, entry_id):
    entry = Entry.objects.get(pk=entry_id)
    headline =entry.headline
    body_text = entry.body_text
    context ={'entry':entry,'headline':headline, 'body_text':body_text}
    return render(request,'editor/look.html', context)
