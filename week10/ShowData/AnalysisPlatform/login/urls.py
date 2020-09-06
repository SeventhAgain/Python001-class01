from django.urls import path,re_path,register_converter
from . import views

urlpatterns = [
    path('hello', views.hello),
    path('register',views.do_reg),
    path('login',views.do_login),

]
