from django.urls import path
from Login_App import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

app_name= 'Login_App'
urlpatterns = [
    path('', views.home_page, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login"),
    path('user_login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="logout")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)