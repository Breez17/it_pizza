"""it_pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from menu.views import *
from sign_up.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('it_pizza/pizzas', it_pizza_pizzas, name='home'),
    path('it_pizza/sign_in/', LoginView.as_view(template_name='log_in.html'),
         name='sign-in'),
    path('it_pizza/sign_out/', LogoutView.as_view(next_page='/'),
         name='log-out'),
    path('it_pizza/sign_up/', it_pizza_sign_up, name='sign-up'),

]
