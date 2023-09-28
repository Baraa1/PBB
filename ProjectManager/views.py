# Python
from datetime import datetime, date
import calendar
import pytz
# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
# Mine
from dockingRecords.models import *
from locations.models import Stand
from accounts.models import CustomUser
from dockingRecords.decorators import *


tz = pytz.timezone('Asia/Riyadh')

@login_required(login_url='login')
@user_passes_test(view_records)
def filter_month(request):
    year = datetime.now().year
    month = datetime.now().month
    # Return a matrix (list of lists) representing a month's calendar.
    # Each row represents a week; week entries are datetime.date values.
    month_calendar = calendar.Calendar()
    month_calendar.setfirstweekday(calendar.SUNDAY)
    month_calendar = calendar.Calendar().monthdatescalendar(year,month)
    weeks_dict = {}
    
    # user filtered chart
    if request.method == 'POST':
        new_date = request.POST.get('month')
        # slice html input type=month
        year = int(new_date[0:4])
        month = int(new_date[5:])
        month_calendar = calendar.Calendar().monthdatescalendar(year, month)

        # get the amounts of records created each week
        for week in month_calendar:
            row = int(month_calendar.index(week))
            weeks_dict[f'Week {row+1}'] = len(DockingRecord.objects.filter(Q(docked__gte = month_calendar[row][0]) & Q(docked__lte = month_calendar[row][6])))

        context = {
                "weeks_dict":weeks_dict,
                "filtered":'true',
            }
        
        return render(request, 'htmx/month-filtered.html', context=context)
    
    # default chart
    for week in month_calendar:
        row = int(month_calendar.index(week))
        weeks_dict[f'Week {row+1}'] = len(DockingRecord.objects.filter(Q(docked__gte = month_calendar[row][0]) & Q(docked__lte = month_calendar[row][6])))

    return weeks_dict, 'false'

@login_required(login_url='login')
@user_passes_test(view_records)
def filter_stands(request):
    stands = Stand.objects.all()
    stands_dict = {}
    
    # user filtered chart
    if request.method == 'POST':
        from_date = request.POST.get('from')
        to_date = request.POST.get('to')
        stand = request.POST.get('stand')
        # if stand specified
        if stand:
            stand_name = Stand.objects.get(id = stand).stand_name
            if from_date:
                if to_date:
                    stands_dict[stand_name] = len(DockingRecord.objects.filter(Q(docked__gte = from_date) & Q(docked__lte = to_date) & Q(stand = stand)))
                else:
                    stands_dict[stand_name] = len(DockingRecord.objects.filter(Q(docked__gte = from_date) & Q(stand = stand)))
            else:
                stands_dict[stand_name] = len(DockingRecord.objects.filter(stand = stand))
        else:
            for stand in stands:
                if from_date:
                    if to_date:
                        stands_dict[stand.stand_name] = len(DockingRecord.objects.filter(Q(stand = stand) & Q(docked__gte = from_date) & Q(docked__lte = to_date)))
                    else:
                        stands_dict[stand.stand_name] = len(DockingRecord.objects.filter(Q(stand = stand) & Q(docked__gte = from_date)))
                elif to_date:
                    stands_dict[stand.stand_name] = len(DockingRecord.objects.filter(Q(stand = stand) & Q(docked__lte = to_date)))
        
        context = {
            "stands": stands,
            "stands_dict": stands_dict,
        }
        return render(request, 'htmx/stands-filtered.html', context=context)

    # default chart
    for stand in stands:
        stands_dict[stand.stand_name] = len(DockingRecord.objects.filter(stand = stand))

    return stands, stands_dict

@login_required(login_url='login')
@user_passes_test(view_records)
def filter_users(request):
    users = CustomUser.objects.filter(Q(is_superuser = False) & Q(Q(groups__name='Operator') | Q(groups__name='Operation Supervisor')))
    users_dict = {}

    if request.method == 'POST':
        from_date = request.POST.get('users-from')
        to_date = request.POST.get('users-to')

        for user in users:
            user2 = SecondOperator.objects.get(second_operator = user)

            if from_date:
                if to_date:# get the records where the date is after from date and before to date and operator1 or operator2 = user 
                    users_dict[f'{user.first_name} {user.last_name}'] = len(DockingRecord.objects.filter(
                            Q(docked__gte = from_date) & Q(docked__lte = to_date) & Q(Q(operator1 = user) | Q(operator2 = user2))
                            )
                        )
                else:
                    users_dict[f'{user.first_name} {user.last_name}'] = len(DockingRecord.objects.filter(
                            Q(docked__gte = from_date) & Q(Q(operator1 = user) | Q(operator2 = user2))
                            )
                        )
            elif to_date:
                users_dict[f'{user.first_name} {user.last_name}'] = len(DockingRecord.objects.filter(
                        Q(docked__lte = to_date) & Q(Q(operator1 = user) | Q(operator2 = user2))
                    )
                )
        context = {
            "users_dict": users_dict,
        }
        return render(request, 'htmx/users-filtered.html', context=context)

    for user in users:
        user2 = SecondOperator.objects.get(second_operator = user)
        users_dict[f'{user.first_name} {user.last_name}'] = len(DockingRecord.objects.filter(Q(operator1 = user) | Q(operator2 = user2)))

    return users_dict

def get_busiest_stand():
    busiest_stand = {'stand':'', 'total':0}
    for stand in Stand.objects.all():
        total_records = len(DockingRecord.objects.filter(stand = stand.id))
        if total_records > busiest_stand['total']:
            busiest_stand['stand'] = stand.gate_name
            busiest_stand['total'] = total_records

    return busiest_stand

def get_busiest_operator():
    busiest_operator = {'name':'', 'total':0}
    for op in CustomUser.objects.filter(Q(is_superuser = False) & Q(Q(groups__name='Operator') | Q(groups__name='Operation Supervisor'))):
        op2 = SecondOperator.objects.get(second_operator = op)
        total_records = len(DockingRecord.objects.filter(Q(operator1 = op.id) | Q(operator2 = op2)))
        if total_records > busiest_operator['total']:
            busiest_operator['name'] = f'{op.first_name} {op.last_name}'
            busiest_operator['total'] = total_records

    return busiest_operator

@login_required(login_url='login')
@user_passes_test(view_records)
def index(request):
    weeks_dict, filtered = filter_month(request)
    stands, stands_dict  = filter_stands(request)
    users_dict           = filter_users(request)
    todays_records       = len(DockingRecord.objects.filter(Q(docked__gte = date.today()) | Q(undocked__gte = date.today())))
    busiest_stand        = get_busiest_stand()
    busiest_operator     = get_busiest_operator()
    total_records        = len(DockingRecord.objects.all())
    total_operators      = len(CustomUser.objects.filter(Q(is_active = True) & Q(is_superuser = False) & Q(Q(groups__name='Operator') | Q(groups__name='Operation Supervisor'))))

    context = {
        "weeks_dict":weeks_dict,
        "filtered":filtered,
        "stands": stands,
        "stands_dict": stands_dict,
        "users_dict": users_dict,
        "todays_records": todays_records,
        "busiest_stand":busiest_stand,
        "busiest_operator":busiest_operator,
        "total_operators":total_operators,
        "total_records":total_records,
    }
    return render(request, 'index.html', context=context)