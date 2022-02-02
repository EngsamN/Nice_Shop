from django.urls import path
from . import views


urlpatterns = [
   #LoginView

path('login/', views.AdminLogin.as_view(), name="login"),
path('logout/', views.logout_view , name='logout'),
path('singup/', views.singupregster,name='singup'),
# singupregster
]
  