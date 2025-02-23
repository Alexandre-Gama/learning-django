from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

# blog/
urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:id>', views.post, name='post'),
    path('postagens/', views.postagens, name='postagens')
]