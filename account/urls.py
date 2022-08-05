from django.urls import path
from . import views
from .views import RegistrationView, LogInView, LogOutView

app_name= 'account'


urlpatterns = [
    path('login/', views.LogInView.as_view(), name='login'),
    path('Registration/', views.RegistrationView.as_view(), name='registration'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
