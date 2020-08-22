学习笔记

## django web开发环境搭建

1. 安装django：`pip install --upgrade django==2.2.13`
2. 安装mysql：`pip install pymysql`
3. 安装gunicorn（用于生产环境发布）：`pip install gunicorn`


## 基本开发规则

1. **配置独立模块**

django开发web项目时，一般将功能较为完整独立的业务放到单独的一个模块中开发。在项目的根目录下创建模块并注册到django中
- `python manage.py startapp index`
- `settings.py`的 `INSTALLED_APPS` 中添加自定义app名

2. **配置数据库**

`settings.py`的 `DATABASES` 中添加自定义app名
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db1',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '192.168.111.130',
        'PORT': '3306',
    }
}
```

`settings.py`同级的 `__init__.py` 文件中添加自定义app名
```python
import pymysql
pymysql.install_as_MySQLdb()
```

3. **配置全局urls**
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('index.urls')),
    path('login/', include('login.urls')),
]
```

4. **添加模块中使用到的静态资源和模板**

字模块中添加文件夹 `static` 和 `templates` 存放静态资源和模板文件。


5. **添加models**

分析业务需求，数据库新建表，然后生成django实体类models

虽然可以通过models生成物理表，但大多数的开发规则还是根据物理表生成models

```
python manage.py inspectdb > app/models.py
```

6. **编写views**

配置子模块urls，并编写views业务逻辑


7. **本地启动项目**

启动前检查urls，views中的配置是否都存在，否则会报错

```
python manage.py runserver
```


## 添加admin后台管理功能

1. **注册admin到django中**

默认已经注册

2. **生成admin需要的表**
```
python manage.py migrate
```
3. **创建管理员账号**
```
python manage.py createsuperuser
```
4. **全局urls中配置好访问路径**

默认配置好
```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    。。。
]
```
5. **将app中的models注册到admin中**

无论有多少个app，都可以按照这种形式注册到admin中
```
from django.contrib import admin

# Register your models here.
from .models import Goods
# 注册模型
admin.site.register(Goods)

```
6. **重启服务**


## 注册、登陆及认证

1. **默认已经注册了auth模块**

之前创建admin的时候，执行的 `python manage.py migrate` 已经生成了相应的user表。

2. **使用django自带的form组件**
```
from django import forms

class regForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    conform_password = forms.CharField(widget=forms.PasswordInput, min_length=8)

class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
```

3. **使用django自带的auth组件**
```python
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# 创建用户
user = User.objects.create_user(input_name, input_name + "@" + input_name + ".com", input_pwd)

# 验证用户
user = authenticate(username=cd['username'], password=cd['password'])
```
