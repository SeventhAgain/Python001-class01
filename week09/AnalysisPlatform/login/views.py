from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from .form import loginForm, regForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt, csrf_protect


def hello(request):
    return HttpResponse("Welcome to use Django!")


# 注册
def do_reg(request):
    # 注册用户
    if request.method == 'POST':
        reg_form = regForm(request.POST)

        if reg_form.is_valid():
            # 读取表单的返回值
            cd = reg_form.cleaned_data

            # 校验两次密码是否一直
            input_name = cd['username']
            input_pwd = cd['password']
            confirm_pwd = cd['conform_password']
            if input_pwd != confirm_pwd:
                return HttpResponse("两次密码输入不一致，注册失败")

            user = User.objects.create_user(input_name, input_name + "@" + input_name + ".com", input_pwd)
            if user:
                return redirect("/auth/login")
            else:
                return HttpResponse('注册失败')

    # 注册页面
    if request.method == "GET":
        reg_form = regForm()
        return render(request, 'reg.html', {'form': reg_form})


# 登陆
def do_login(request):
    # 登陆
    if request.method == 'POST':
        login_form = loginForm(request.POST)

        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data

            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse('登陆成功')
            else:
                return HttpResponse('登陆失败')

    # 登陆页面
    if request.method == "GET":
        login_form = loginForm()
        return render(request, 'login.html', {'form': login_form})
