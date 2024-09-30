from django.urls import path
from Login_App import views

app_name= 'Login_App'
urlpatterns = [
    path('', views.home_page, name="home"),
    path('register/', views.register, name="register")
]
