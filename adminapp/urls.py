from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_login, name='redirect_to_login'),
    path('login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('blogs/',views.blogs, name="blogs"),
    path('add_blog/',views.add_blog, name="add_blog"),
    path('message_list/', views.message_list, name='message_list'),
    path('message_detail/<int:pk>/', views.message_detail, name='message_detail'),
    path('blogs/delete/<int:pk>/', views.delete_blog, name='delete_blog'),
]