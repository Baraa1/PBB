from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    # Accounts
    path('', accounts, name='accounts'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('search_accounts/', search_accounts, name='search_accounts'),
    path('create_account/', create_account, name='create_account'),
    path('update_account/<int:pk>/', update_account, name='update_account'),
    path('delete_account/<int:pk>/', delete_account, name='delete_account'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('deactivate_account/<int:pk>/', deactivate_account, name='deactivate_account'),
    # Password
    path('password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name            = 'password/password_reset.html',
            html_email_template_name = 'email/password_reset_email.html',
            subject_template_name    = 'email/password_reset_subject.txt',
            ),
            name                     = 'password_reset'
        ),
    path('password_reset_done/', password_reset_done, name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            # success_url   = 'sign_in',
            template_name = 'password/password_reset_confirm.html',
            ),
            name          = 'password_reset_confirm'
        ),
    path('reset/done/', password_reset_complete, name = 'password_reset_complete'),
    path('password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name = 'password/password_change.html',
            ),
            name          = 'password_change'
        ),
    path('password_change_done/', password_change_done, name = 'password_change_done'),
    # Job Description
    #path('create_job_description/<int:pk>/', create_job_description, name='create_job_description'),
    #path('update_job_description/<int:pk>/', update_job_description, name='update_job_description'),
]