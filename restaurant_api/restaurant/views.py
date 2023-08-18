from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from rest_framework.decorators import permission_classes
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from .models import Restaurant, Menu, Employee
from .serializers import RestaurantSerializer, MenuSerializer, EmployeeSerializer
from .permissions import IsAdminOrReadOnly


# API view for listing and creating restaurants
class RestaurantAPIList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsAdminOrReadOnly,)  # Custom permission: Admin can modify, others can read

# API view for listing and creating employees
class EmployeeAPIList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminOrReadOnly,)  # Custom permission: Admin can modify, others can read

# API view for listing and creating menus
class MenuAPIList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsAdminOrReadOnly,)  # Custom permission: Admin can modify, others can read

# API view for retrieving, updating, and deleting a specific restaurant
class RestaurantUpdateDestroyAPIList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsAdminUser,)  # Only admin users can modify or delete

# API view for retrieving, updating, and deleting a specific employee
class EmployeeUpdateDestroyAPIList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminUser,)  # Only admin users can modify or delete

# API view for retrieving, updating, and deleting a specific menu
class MenuUpdateDestroyAPIList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsAdminUser,)  # Only admin users can modify or delete

@permission_classes([IsAuthenticated])
def employee_voting(request, employee_id, menu_id):
    '''Function that check employee to be from same restaurant as menu, and providing vote system'''
    # Getting employee and menu objects and check requirements
    employee = get_object_or_404(Employee, id=employee_id)
    menu = get_object_or_404(Menu, id=menu_id)
    if employee.employee_restaurant != menu.menu_restaurant:
        return redirect('http://127.0.0.1:8000/api/restaurant/')
    elif int(employee.employee_vote) >= 1:
        return redirect(f'http://127.0.0.1:8000/api/employee/{employee.pk}')

    # Adding vote
    menu.menu_vote_count += 1
    employee.employee_vote += 1

    # Saving vote
    menu.save()
    employee.save()
    
    # Redirect to a success page or a menu details page
    return redirect('http://127.0.0.1:8000/api/menu/')

@permission_classes([AllowAny])
def today_menu(request):
    '''Function provide redirect to the menu page with biggest amount of votes'''
    # Retrieve today's date
    today = timezone.now().date()
    
    # Get first today's menu with biggest vote count
    most_voted_menu = Menu.objects.filter(menu_created_at__date=today).order_by('-menu_vote_count').first()
    
    # Redirect to page with today's menu
    return redirect(f'http://127.0.0.1:8000/api/menu/{most_voted_menu.pk}/')
