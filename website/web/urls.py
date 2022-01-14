from django.urls import path
from .import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),  #the name is a shortcut to the actual path
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
