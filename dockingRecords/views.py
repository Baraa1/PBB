# Django Classes
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from pathlib import Path
# My Classes
from .decorators import *
from ProjectManager.decorators import *
from .models import DockingRecord, SecondOperator
from .forms import *
from .filters import *
from .excel import by_record_filter
# Python
import requests
import json
from pathlib import Path

JSON_DIR = Path(__file__).resolve().parent

################################################################################################################################################################################
############################################################################# Records ##########################################################################################
################################################################################################################################################################################

@login_required(login_url='login')
@user_passes_test(view_records)
def flight_schedule(request):
    return render(request,"flight-schedule.html")

@login_required(login_url='login')
@user_passes_test(view_records)
def dockings(request):
    # limits records sent to the latest 20
    records_filter = RecordFilter(request.GET, DockingRecord.objects.filter())
    docking_records = DockingRecord.objects.all().order_by('-time_stamp')[:20]

    #if the user issued a filter request return the filtered data
    if request.method == "POST":
        # limite the results to protect the server from stupid enquiries that result in thousands of results
        record_filter = RecordFilter(request.POST, DockingRecord.objects.filter())
        if len(record_filter.qs) > 1000:
            #messages.warning(request, f"Too many Results {len(record_filter)}, try a more specific filter")
            context = {
                "docking_records":DockingRecord.objects.none(),
                "records_filter":records_filter,
                "total_records":f'Too many Results {len(record_filter.qs)}, try a more specific filter',
                }
            return render(request,'tables/docking-records-table.html', context)

        context = {
            "docking_records": record_filter.qs,
            "records_filter":records_filter,
            "total_records":len(record_filter.qs),
            }

        return render(request,'tables/docking-records-table.html', context)
    # else return all records
    context = {
        "docking_records":docking_records,
        "records_filter":records_filter,
        "total_records":len(docking_records),
        }
    return render(request,"dockings.html",context)

@login_required(login_url='login')
@user_passes_test(view_records)
def arrival_schedule(request):
    # get the sheduled flights list created by crontab
    fids_context = {}
    with open(f'{JSON_DIR}/json/fids_arr_dict.json') as f:
        fids_context['arr_schedule'] = json.load(f)

    return render(request,"arr_fids.html",fids_context)

@login_required(login_url='login')
@user_passes_test(view_records)
def departure_schedule(request):
    # get the sheduled flights list created by crontab
    fids_context = {}
    with open(f'{JSON_DIR}/json/fids_dep_dict.json') as f:
        fids_context['dep_schedule'] = json.load(f)

    return render(request,"dep_fids.html",fids_context)

@login_required(login_url='login')
@user_passes_test(view_records)
def search_records(request):
    if request.method == "POST":
        search_field  = request.POST.get('search-radios')
        record_filter = filter_records(request.POST.get('search-bar'),search_field)
        context       = {
            "docking_records": record_filter,
            "total_records":len(record_filter),
            }
    return render(request,'tables/docking-records-table.html', context)


@login_required(login_url='login')
@user_passes_test(add_records)
def create_docking_fids(request, iata):
    params = {
        'api_key': 'c5076a67-e3d7-474e-8f46-dc3949b2c9e4',
        'flight_iata': iata,
        'extra':'estimated',
        '_fields':'aircraft_icao,reg_number'
    }
    # request endpoint: schedules
    api_base = 'https://airlabs.co/api/v9/flights'
    api_result = requests.get(api_base, params)
    api_response = api_result.json()
    print(api_response)
    if request.method == 'POST':
        form = CreateDockingForm(request.POST, request=request)
        if form.is_valid():
            instance = form.save(commit=False)
            # saves the record to the logged in user in case they changed it in the browser
            instance.operator1 = CustomUser.objects.get(id = request.user.id)
            instance.save()
            return redirect('dockings')
    else:
        form = CreateDockingForm(initial={
            'flight_no1': iata,
            'ac_type': api_response['response'][0]['aircraft_icao'],
            'ac_reg': api_response['response'][0]['reg_number'],
        }, request=request)

    context = {
        "form":form,
        "current_user":request.user
        }

    return render(request,"create-docking.html",context)

@login_required(login_url='login')
@user_passes_test(add_records)
def create_docking(request):
    if request.method == 'POST':
        form = CreateDockingForm(request.POST, request=request)
        if form.is_valid():
            instance = form.save(commit=False)
            # saves the record to the logged in user in case they changed it in the browser
            instance.operator1 = CustomUser.objects.get(id = request.user.id)
            instance.save()
            return redirect('dockings')
    else:
        form = CreateDockingForm(request=request)

    context = {
        "form":form,
        # to show the username to the end user
        "current_user":request.user
        }

    return render(request,"create-docking.html",context)

@login_required(login_url='login')
@user_passes_test(add_records)
def create_nodocking(request):
    current_user = SecondOperator.objects.get(second_operator__id = request.user.id)
    if request.method == 'POST':
        form = CreateNoDockingForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # saves the record to the logged in user in case they changed it in the browser
            instance.operator2 = current_user
            instance.no_docking = True
            instance.save()
            return redirect('dockings')
    else:
        form = CreateNoDockingForm()

    context = {
        "form":form,
        "current_user":current_user,
        }

    return render(request,"create-nodocking.html",context)

# This is actually an update Function
@login_required(login_url='login')
@user_passes_test(add_records)
def create_undocking(request, pk):
    record = get_object_or_404(DockingRecord, id = pk)

    if request.method == 'POST':
        form = CreateUndockingForm(request.POST, instance = record)
        if form.is_valid():
            instance = form.save(commit=False)
            user = CustomUser.objects.get(id = request.user.id)
            instance.operator2 = SecondOperator.objects.get(second_operator = user)
            instance.save()
            return redirect('dockings')
    else:
        form = CreateUndockingForm(instance=record)

    context = {
        "form":form,
        "current_user":request.user
        }

    return render(request,"create-undocking.html",context)

@login_required(login_url='login')
@user_passes_test(update_records)
def update_record(request, pk):
    record = get_object_or_404(DockingRecord, id = pk)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance = record)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('dockings')
    else:
        form = UpdateRecordForm(instance=record)

    context = {
        "form":form,
        }

    return render(request,"update-record.html",context)

@login_required(login_url='login')
@user_passes_test(view_records)
def view_record(request, pk):
    record = get_object_or_404(DockingRecord, id = pk)

    context = {
        "record":record,
        }

    return render(request,"view-record.html",context)

@login_required(login_url='sign_in')
@user_passes_test(update_records)
def export_search_logs(request):
    record_filter = RecordFilter(request.POST, DockingRecord.objects.filter().order_by('-id'))
    response = by_record_filter(record_filter)

    return response
############## DANGER SIGNS HERE!!!! ###################

#def copy_users(request):
#    users = CustomUser.objects.all()
#    for user in users:
#        new_user = SecondOperator(second_operator = user)
#        new_user.save()
#
#    return redirect('accounts')