from django.db import models


# Model for representing a restaurant
class Restaurant(models.Model):
    restaurant_title = models.CharField(max_length=255)  # Title of the restaurant
    restaurant_place = models.CharField(max_length=255)  # Place/location of the restaurant

# Model for representing an employee
class Employee(models.Model):
    employee_restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, null=False)
    # Relationship to the associated Restaurant model using a ForeignKey
    employee_registeration_time = models.DateTimeField(auto_now_add=True)  # Registration timestamp
    employee_first_name = models.CharField(max_length=255)  # First name of the employee
    employee_last_name = models.CharField(max_length=255)  # Last name of the employee
    employee_vote = models.IntegerField(default=0)  # Number of votes received by the employee

# Model for representing a menu
class Menu(models.Model):
    menu_restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, null=False)
    # Relationship to the associated Restaurant model using a ForeignKey
    menu_created_at = models.DateTimeField(auto_now_add=True)  # Creation timestamp of the menu
    menu_title = models.CharField(max_length=255)  # Title of the menu
    menu_text = models.TextField(max_length=3000)  # Text content of the menu
    menu_vote_count = models.IntegerField(default=0)  # Number of votes received by the menu

 