from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_user_view, name='add_user'),
    path('display-users/', views.display_users_view, name='display_users'),
    path('update/<int:id>/', views.update_user_view, name='update'),
    path('delete/<int:id>/', views.delete_user_view, name='delete'),
]
