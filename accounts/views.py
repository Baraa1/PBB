# Django
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from datetime import date

# login function renamed because my view is called login too 
from django.contrib.auth import logout as auth_logout, login as auth_login
# Custom
from .models import CustomUser
from .forms import *
from .filters import *
from ProjectManager.decorators import *
from .decorators import *
from dockingRecords.models import DockingRecord, SecondOperator

################################################################################################################################################################################
############################################################################# Accounts #########################################################################################
################################################################################################################################################################################

### user is reserved for the logged in user.
### account is for other users

@login_required(login_url='login')
@user_passes_test(view_accounts)
def accounts(request):
    # initial filter, filters accounts in the same terminal or group as the user depending on the user group 
    account_filter = UserFilter(request.GET, CustomUser.objects.filter(is_superuser = False, location = request.user.location).distinct().order_by('groups'))

    # filtered users
    if request.method == "POST":
        #terminal = Terminal.objects.get(terminal_name = request.POST.get('terminal'))
        account_filter = UserFilter(request.POST, CustomUser.objects.filter(is_superuser = False).distinct().order_by('groups'))
        context     = {"accounts": account_filter.qs}

        return render(request,'accounts/tables/users-table.html', context)

    # else return all users data
    context = {
        "accounts":account_filter.qs,
        "account_filter": account_filter,
        }

    return render(request,"accounts/accounts.html",context)

@login_required(login_url='login')
@user_passes_test(view_accounts)
def search_accounts(request):
    search_field  = request.POST.get('search-radios')
    record_filter = filter_accounts(request.POST.get('search-bar'), search_field)
    context       = {"accounts": record_filter}
    return render(request,'accounts/tables/accounts-table.html', context)

@login_required(login_url='login')
@user_passes_test(add_accounts)
def create_account(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # to add an admin account
            #instance.is_staff = True
            #instance.is_superuser = True
            instance.set_password(form.cleaned_data['password'])
            instance.save()
            new_user = instance
            form.save_m2m()
            SecondOperator.objects.create(second_operator = new_user)
            messages.info(request, f"{form.cleaned_data['username']} - ID: {form.cleaned_data['user_id']} Account was created successfuly.")
            return redirect('accounts')
    else:
        form = CreateUserForm()

    context = {
        "form":form,
        }

    return render(request,"accounts/create-account.html",context)

@login_required(login_url='login')
@user_passes_test(update_accounts)
def update_account(request, pk):
    account = get_object_or_404(CustomUser, id = pk)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST,instance=account)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()
            messages.info(request, f'{account.username} was successfully edited')
            return redirect('accounts')
    else:
        form = UpdateUserForm(instance=account)
    
    context = {
        'form': form,
        # sending the id for the delete account btn
        'accountid':account.id
    }

    return render(request, 'accounts/update-account.html', context)

@login_required(login_url='login')
@user_passes_test(delete_accounts)
def delete_account(request,pk):
    account = get_object_or_404(CustomUser, id = pk)
    account.delete()
    messages.success(request, f'{account.username} Account and all records related to it were deleted')
    return redirect('accounts')

# HTMX function
# The toggle switch is created using Bootstrap
# the Toggle switch in the view users page displays a modal using Bootstrap CSS
# the model has 2 btns cancel and Activate or Deactivate
# the btns issue an HTMX post request to this function
# this function changes the active status of the user and return a new check box field
# the HTMX function then replace the old check box with the new one
# by targeting it using the custom id created by django template tags
# using JS the modal text will be fixed to match the new user status
@login_required(login_url='login')
@user_passes_test(update_accounts)
def deactivate_account(request, pk):
    account = get_object_or_404(CustomUser, id = pk)

    if request.method == 'POST':
        account.is_active = False if account.is_active else True
        account.save()
        return render(request, 'accounts/htmx/check-box.html', {'account':account})

    return render(request, 'accounts/htmx/check-box.html', {'account':account})

    ######### this was for the toggle switch alone before the modal #############
    #    form = DeactivateUserForm(request.POST,instance=user)
    #    if form.is_valid():
    #        # dont save before editing the active status
    #        instance = form.save(commit=False)
    #                #if instance.is_active == ['on']:
    #                #    instance.is_active = False
    #                #else:
    #                #    instance.is_active = True
    #                # This line of code replaces the above lines
    #                #  instance.is_active = request.POST.getlist(f'{user.username}flexSwitchCheckChecked')
    #                #  instance.is_active = False if instance.is_active == ['on'] else True
    #                #  instance.save()
    # returns nothing
    # return HttpResponse('')

def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.POST and form.is_valid():
        form = LoginForm(request.POST)
        user = form.login(request)
        if user is not None:
            auth_login(request, user)
            # send operators to records page
            if request.user.groups.filter(name='Operator').exists() or request.user.groups.filter(name='Operation Supervisor').exists():
                # Redirect to a success page.
                return redirect('dockings')

            return redirect('index')
    
    form = LoginForm(None)
    context = {
        "form":form,
        }

    return render(request, 'accounts/login.html', context)

@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    messages.success(request, "You were successfully logged out.")
    return redirect('login')

#forgot_Password email sent
def password_reset_done(request):
    messages.info(request, "If there's an account connected to the provided E-Mail, you will recieve a link to reset your password")
    return redirect('login')

#forgot_Password reset Done
def password_reset_complete(request):
    messages.info(request, "Password reset complete.")
    return redirect('login')

@login_required(login_url='login')
def password_change_done(request):
    messages.info(request, "Your Password was successfully changed.")
    return redirect('index')

@login_required(login_url='login')
def profile(request, pk):
    account           = get_object_or_404(CustomUser, id = pk)
    all_logs          = len(DockingRecord.objects.all())
    account2          = SecondOperator.objects.get(second_operator = account)
    total_logs        = len(DockingRecord.objects.filter(Q(operator1 = account) | Q(operator2 = account2)))
    todays_records    = len(DockingRecord.objects.filter(
        Q(Q(operator1 = account ,docked__gte = date.today()) | Q(operator1 = account, undocked__gte = date.today())) |
        Q(Q(operator2 = account2 ,docked__gte = date.today()) | Q(operator2 = account2, undocked__gte = date.today()))
        )
    )
    employee_prcntg = ((total_logs/all_logs)*100)
    context = {
        'account': account,
        'total_logs': total_logs,
        'todays_records':todays_records,
        'employee_prcntg':employee_prcntg,
        }
    return render(request, 'accounts/profile.html', context)