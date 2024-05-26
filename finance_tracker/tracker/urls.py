from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('edit_transaction/<int:pk>/', views.edit_transaction, name='edit_transaction'),
    path('delete_transaction/<int:pk>/', views.delete_transaction, name='delete_transaction'),
    path('signup/', views.signup_view, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='signin.html'), name='signin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
