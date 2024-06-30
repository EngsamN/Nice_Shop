from django.urls import path
from . import views
from .views import example_view


urlpatterns = [
   #LoginView

path('login/', views.AdminLogin.as_view(), name="login"),
path('logout/', views.logout_view , name='logout'),
path('singup/', views.singupregster,name='singup'),
path('example/', example_view, name='example_view'),

# singupregster
]
