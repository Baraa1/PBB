from django.urls import path

from .views import *

urlpatterns = [
    # Accounts
    path('upload_accounts_file/', upload_accounts_file, name='upload_accounts_file'),
    path('delete_accounts_file/<int:file_id>', delete_accounts_file, name='delete_accounts_file'),
    path('import_accounts_data/<int:file_id>/', import_accounts_data, name='import_accounts_data'),
    path('acc_template/', acc_template, name='acc_template'),
    # Dcocking Records
    path('upload_records_file', upload_records_file, name='upload_records_file'),
    path('delete_records_file/<int:file_id>', delete_records_file, name='delete_records_file'),
    path('import_records_data/<int:file_id>/', import_records_data, name='import_records_data'),
    path('rec_template', rec_template, name='rec_template'),
    # Locations
    path('upload_location_file/', upload_location_file, name='upload_location_file'),
    path('delete_location_file/<int:file_id>', delete_location_file, name='delete_location_file'),
    path('import_location_data/<int:file_id>/', import_location_data, name='import_location_data'),
    path('locations_template/', locations_template, name='locations_template'),
]