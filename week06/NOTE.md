学习笔记

## django创建项目、启动及常用操作
```shell script
django-admin startproject project_name

# manage.py相关命令
python manage.py help

# 创建app（建议不同得功能拆分成不同的app）
python manage.py startapp app_name

# 启动
python manage.py runserver
python manage.py runserver 127.0.0.1:9999

# model -> table
python manage.py makemigrations
python manage.py migrate

# table -> model
python manage.py inspectdb > models.py

```

## django项目目录结构

- project_name(项目名)
    - project_name (项目系统设置)
        + __init__.py (系统初始加载文件)
        + settings.py (系统设置)
        + urls (全局路由)
        + wsgi.py
    - app1（应用1）
        + migrations
        + static (静态资源)
        + templates (模板文件)
        + __init__.py (应用初始加载文件)
        + models.py (数据库表对应实体类)
        + views.py (业务层)
        + urls.py (应用路由)
    - app2（应用2）
        + 。。。

关于django MTV模式的理解：

1. urls可以理解为请求路径：全局urls类似Java Controller类上的路径，app的urls类似methods上的路劲，最终会叠加
2. views可以理解为业务层，接收请求-> 获取数据 -> 数据处理 -> 数据展示（json/html)
3. models可以理解为数据库表对应的实体类
4. template可以理解为Java web开发中的模板，可以有`JSP`、`FreeMarker`、`Thymeleaf`等，接收数据并展示。前后端分离模式流行后该部分一般拆分出去。


## 关于包和模块的引用

1. 一个py文件就是一个模板
2. 多个模板放在一个文件夹下就是一个包

使用：

- 模板单独运行时 if __name__ == '__main__' 会执行，当模块被引入时不执行
- 导入包：import package_name.module_name.method_name as simple_name 
- 导入包：from package_name import module as m1 
- 包内模块间引入：from . import module2
- 包内引入子包：from .package2 import module2 as m2


## ORM API
Django中文文档：[https://docs.djangoproject.com/zh-hans/2.2/](https://docs.djangoproject.com/zh-hans/2.2/)





