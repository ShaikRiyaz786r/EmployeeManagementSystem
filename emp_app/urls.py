from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('view_emp/', view_emp, name='view_emp'),
    path('add_emp/', add_emp, name='add_emp'),
    path('remove_emp/', remove_emp, name='remove_emp'),
    path('update_emp/', update_emp, name='update_emp'),
    path('filter_emp/', filter_emp, name='filter_emp'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('update/<int:pk>/', update, name='update'),
]
