
from re import template

from dashboard import views as dash_views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('register/', dash_views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="dashboard/login.html"),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="dashboard/logout.html"),name='logout'),

]
