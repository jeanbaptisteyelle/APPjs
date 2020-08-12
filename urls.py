from django.urls import path

from . import views
urlpatterns = [

    path('', views.index, name='index'),

    path('appointment', views.appointment, name='appointment'),

    path('blog-single', views.blog_single, name='blog-single'),

    path('login', views.login, name='login'),

    path('register', views.register, name='register'),
    
    path('postdata', views.postdata, name='postdata'),
    
    path('is_login', views.is_login, name='is_login'),

]