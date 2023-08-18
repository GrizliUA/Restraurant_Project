from django.contrib import admin

from .models import Restaurant, Menu, Employee

# Register the Restaurant model with the Django admin interface
admin.site.register(Restaurant)

# Register the Employee model with the Django admin interface
admin.site.register(Employee)

# Register the Menu model with the Django admin interface
admin.site.register(Menu)
