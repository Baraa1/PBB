from django.urls import path

from .views import *

urlpatterns = [
    # Records
    path('', roster, name='roster'),
    path('create_shift/', create_shift, name='create_shift'),
    path('assign_shift/', assign_shift, name='assign_shift'),
    path('get_assignment/', get_assignment, name='get_assignment'),
    path('update_assignment/<int:pk>/', update_assignment, name='update_assignment'),
    path('delete_assignment/<int:pk>', delete_assignment, name='delete_assignment'),
    path('get_records/', get_records, name='get_records'),
    path('my_roster/<int:pk>/', my_roster, name='my_roster'),
]