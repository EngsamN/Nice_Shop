from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('brand/', views.brandsview, name='brand'),
    path('index/', views.dashboard, name='index'),
    path('product/', views.prodef, name='product'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('brandetail/<int:id>',views.brandetail,name='brandetail'), 
    path('create_view/',views.create_view,name='create_view'),
    path('admin/', admin.site.urls),
  
]
