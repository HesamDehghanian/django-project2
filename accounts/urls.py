from django.urls import path

from . import views


urlpatterns = [
    path('profile/edit', views.edit_user_profile, name='edit_profile'),
    path('user/', views.user_dashboard, name='user_dashboard'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('superadmin/', views.superadmin_dashboard, name='superadmin_dashboard'),
]
