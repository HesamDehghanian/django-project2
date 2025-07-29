from django.urls import path
from .views import edit_user_profile

urlpatterns = [
    path('accounts/profile/', edit_user_profile, name='edit_profile'),
]