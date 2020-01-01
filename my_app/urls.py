from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('delete/<inv_id>',views.delete,name='delete'),
    path('add_investment/',views.add_inv,name='add'),
    path('graph/',views.graph,name='graph')
]
