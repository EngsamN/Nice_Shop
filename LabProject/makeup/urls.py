from django.urls import path
from . import views

urlpatterns = [
    path('brand/', views.brandsview, name='brand'),
    path('index/', views.dashboard, name='index'),
    path('product/', views.prodef, name='product'),
    path('detail/<int:id>',views.detail,name='detail'), 
    # <int:id>
]
