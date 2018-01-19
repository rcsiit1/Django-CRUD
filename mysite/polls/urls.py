from django.urls import path,re_path

from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('create/', views.create, name='create'),
    path('update/', views.update, name='update'),
    path('insert/', views.insert, name='insert'),
    path('store/', views.store, name='store'),
]