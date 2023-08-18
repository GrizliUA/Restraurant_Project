from rest_framework import serializers
from .models import Restaurant, Menu, Employee


# Serializer for the Restaurant model
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
      model = Restaurant
      fields = ('restaurant_title', 'restaurant_place')
      # Include specified fields from the model

# Serializer for the Employee model
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
      model = Employee
      fields = ('employee_restaurant', 'employee_first_name', 'employee_last_name', 'employee_vote')
      # Include specified fields from the model

# Serializer for the Menu model
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
      model = Menu
      fields = ('menu_restaurant', 'menu_title', 'menu_text', 'menu_vote_count')
      # Include specified fields from the model