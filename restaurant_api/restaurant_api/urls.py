"""
URL configuration for restaurant_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from restaurant.views import *


urlpatterns = [
    #Authorization urls
    path('admin/', admin.site.urls),
    path('api/site-auth/',include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    #Creating Restaurant urls
    path('api/restaurant/', RestaurantAPIList.as_view()),
    path('api/restaurant/<int:pk>/', RestaurantUpdateDestroyAPIList.as_view()),

    #Adding Menu urls
    path('api/menu/', MenuAPIList.as_view()),
    path('api/menu/<int:pk>/', MenuUpdateDestroyAPIList.as_view()),
    
    #Creating Employee urls
    path('api/employee/', EmployeeAPIList.as_view()),
    path('api/employee/<int:pk>/', EmployeeUpdateDestroyAPIList.as_view()),


    #Getting current day menu url
    path('api/today/menu/', today_menu),

    #Employee voting url
    path('api/vote/<int:employee_id>/<int:menu_id>/', employee_voting),

    #Getting results for the current day url
    path('api/today/top/', today_menu),
]
