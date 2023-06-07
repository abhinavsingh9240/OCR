from django.urls import path

from home import views
from django.contrib.auth import views as auth_views

from home.views import PasswordsChangeView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name='logout'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('search/', views.search, name="search"),
    path('uploads/', views.uploads, name="uploads"),
    path('uploads/delete/<int:id>/', views.delete, ),
    path('uploads/<int:id>/', views.show),
    path('settings/', views.settings, name="settings"),
    path('settings/username', views.username),
    path('settings/password', PasswordsChangeView.as_view(template_name="password.html")),
    path('settings/name',views.name),
    path('settings/delete',views.delete_user),
]
