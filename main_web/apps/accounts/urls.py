from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name="accounts"
urlpatterns = [
    
    # Django Auth
    path('login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name='logout'),

    # Customers PATH
    path('customers', views.CustomerView,name="customers"),
    path('customersAdd', views.customerViewAdd,name="customersAdd"),
    path('customersEdit/<pk>', views.costumerViewEdit,name="customersEdit"),
    
    #Employee PATH
    path('employee', views.employeeView,name="employee"),
    path('employeeAdd', views.employeeViewAdd,name="employeeAdd"),
    path('employeeEdit/<pk>', views.employeeViewEdit,name="employeeEdit"),
]
