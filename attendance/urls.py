from django.urls import path

from .views import *

urlpatterns = [
    # Records
    path('', roster, name='roster'),
    path('filter_roster_by_accounts', filter_roster_by_accounts, name='filter_roster_by_accounts'),
    path('create_attendance_record/', create_attendance_record, name='create_attendance_record'),
    path('get_attendance_record/', get_attendance_record, name='get_attendance_record'),
    path('update_attendance_record/<int:pk>/', update_attendance_record, name='update_attendance_record'),
    path('delete_attendance_record/<int:pk>', delete_attendance_record, name='delete_attendance_record'),
    path('get_records/', get_records, name='get_records'),
    path('account_roster/<int:pk>/', account_roster, name='account_roster'),
    path('create_shift/', create_shift, name='create_shift'),
]