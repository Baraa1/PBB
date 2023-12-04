from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from accounts.models import CustomUser
from .models import Shift, AttendanceRecord
from .filters import *
from accounts.filters import UserFilter
from .forms import *
from django.http import HttpResponse
from datetime import datetime
import calendar
from django.db.models import Q

#, timezone='Asia/Riyadh'
def get_month_dates(year, month):
    calendar.setfirstweekday(calendar.SUNDAY)

    cal = calendar.monthcalendar(year, month)

    # Create a list to store the dates
    month_dates = []

    # Iterate over each week in the calendar
    for week in cal:
        # Iterate over each day in the week
        for day in week:
            # Exclude days that belong to the previous or next month
            if day != 0:
                # Append the date to the list
                dd = datetime(year, month, day, 0, 0, 0)
                month_dates.append(dd.date())
                #date_object = datetime(year, month, day, tzinfo=pytz.timezone(timezone))
                # Append the datetime object to the list
                #month_dates.append(date_object)

    return month_dates
def get_week_dates(year, month):
    month_days     = calendar.Calendar()
    month_days.setfirstweekday(calendar.SUNDAY)
    days_generator = month_days.itermonthdates(year,month)
    days           = []
    for day in days_generator:
        days.append(day)

    return days

def filter_records_by_month(month_records, dates, account_filter):
    filtered_records = []
    for employee in account_filter:
        temp_list = []
        temp_list.append(employee.id)
        temp_list.append(f'{employee.first_name} {employee.last_name}')
        roles = []
        for role in employee.groups.all():
            roles.append(f'{role}')
        temp_list.append(roles)

        for day in dates:
            try:
                temp_list.append(month_records.get(employee = employee, date = day))
            except AttendanceRecord.DoesNotExist:
                temp_list.append(day)
        filtered_records.append(temp_list)
    return filtered_records

@login_required(login_url='login')
@permission_required(['attendance.view_attendancerecord','attendance.add_attendancerecord','attendance.change_attendancerecord','attendance.delete_attendancerecord',], raise_exception=True)
def roster(request):
    '''
        Creates a table for the current or chosen month and year with filters and wait for the user input
    '''
    account_filter = UserFilter(request.GET, CustomUser.objects.filter(is_superuser = False, is_active = True).distinct().order_by('groups'))
    shifts         = Shift.objects.all()
    form           = CreateAttendanceRecordForm()
    selected_month = request.GET.get("selected_month")
    selected_year  = request.GET.get("selected_year")

    if selected_month == None or selected_year == None:
        selected_year = datetime.now().year
        selected_month = datetime.now().month
    else:
        selected_year = int(selected_year)
        selected_month = int(selected_month)
    dates          = get_month_dates(selected_year, selected_month)

    context = {
        "account_filter":account_filter,
        "shifts":shifts,
        "selected_year":selected_year,
        "selected_month":selected_month,
        "dates":dates,
        "form":form,
    }
    
    return render(request,"attendance-records/roster.html", context)

@login_required(login_url='login')
@permission_required(['attendance.view_attendancerecord','attendance.add_attendancerecord','attendance.change_attendancerecord','attendance.delete_attendancerecord',], raise_exception=True)
def filter_roster_by_accounts(request):
    # Get the month and year from the request and generate month dates in proper format
    selected_month = int(request.GET.get("selected_month"))
    selected_year  = int(request.GET.get("selected_year"))
    dates          = get_month_dates(selected_year, selected_month)
    form           = CreateAttendanceRecordForm()

    if request.method == "POST":
        account_filter = UserFilter(request.POST, CustomUser.objects.filter(is_superuser = False, is_active = True).distinct().order_by('groups'))
        # Get all the records for the selected user group in the specified date
        month_records = AttendanceRecord.objects.filter(Q(employee__in=account_filter.qs) & Q(date__month=selected_month) & Q(date__year = selected_year))
        # returns a list of account lists that contains either an attendance record or a datetime object to be used for filling the roster table 
        filtered_records = filter_records_by_month(month_records, dates, account_filter.qs)
        context = {
            "filtered_records": filtered_records,
            "form": form,
            "htmx": True,
        }
        return render(request,"attendance-records/tables/roster-table2.html", context)
    return HttpResponse(status=500)

@login_required(login_url='login')
@permission_required('attendance.add_attendancerecord', raise_exception=True)
def create_attendance_record(request):
    if request.method == 'POST':
        form = CreateAttendanceRecordForm(request.POST)

        if form.is_valid():
            form.save()
            record = form.instance
            context = {"record":record,"form":form}
            return render(request,"attendance-records/includes/update-record.html", context)

    return HttpResponse(status=500)

# Unused right now
@login_required(login_url='login')
@permission_required('attendance.view_attendancerecord', raise_exception=True)
def get_attendance_record(request):
    employee_id = request.GET.get("employee_id")
    shift_date  = request.GET.get("shift_date")
    assignment  = get_object_or_404(AttendanceRecord, employee_id = employee_id, date=shift_date)
    form        = CreateAttendanceRecordForm(instance = assignment)

    context = {"record":assignment,"form":form}
    return render(request,"attendance-records/includes/attendance-record.html", context)


@login_required(login_url='login')
@permission_required('attendance.change_attendancerecord', raise_exception=True)
def update_attendance_record(request, pk):
    assignment = get_object_or_404(AttendanceRecord, id = pk)

    if request.method == 'POST':
        form = CreateAttendanceRecordForm(request.POST, instance = assignment)
        if form.is_valid():
            form.save()
            record = form.instance
            form = CreateAttendanceRecordForm(instance = record)
            context = {
                "record":record,
                "form":form,
                }
            return render(request,"attendance-records/includes/update-record.html", context)
    else:
        return HttpResponse(status=500)

@login_required(login_url='login')
@permission_required('attendance.delete_attendancerecord', raise_exception=True)
def delete_attendance_record(request, pk):
    record = get_object_or_404(AttendanceRecord, id = pk)
    employee_id = record.employee.id
    shift_date  = record.date#'{:02d}'.format(record.date.day)
    record.delete()
    form        = CreateAttendanceRecordForm()
    context = {
        "form":form,
        "employee_id":employee_id,
        "shift_date":shift_date,
        }
    return render(request,"attendance-records/includes/deleted-record.html",context)

@login_required(login_url='login')
@permission_required('attendance.view_attendancerecord', raise_exception=True)
def get_records(request):
    shift_id     = request.GET.get("shift_id")
    shift_date   = request.GET.get("shift_date")
    
    context = {
        "shift_name":Shift.objects.get(id = shift_id).name,
        "shift_date":shift_date,
        "shift_id":shift_id,
    }
    return render(request,"attendance-records/includes/records.html", context)

@login_required(login_url='login')
@permission_required('attendance.view_attendancerecord', raise_exception=True)
def account_roster(request, pk):
    selected_month = request.GET.get("selected_month")
    selected_year  = request.GET.get("selected_year")
    if selected_month == None or selected_year == None:
        selected_year = datetime.now().year
        selected_month = datetime.now().month
    else:
        selected_year = int(selected_year)
        selected_month = int(selected_month)

    prev_month = selected_month-1 if selected_month > 1 else 12
    prev_year  = selected_year-1 if selected_month == 1 else selected_year

    dates = get_week_dates(selected_year, selected_month)
    records  = AttendanceRecord.objects.filter(
        Q(employee__id = pk) &
        Q(Q(date__month=selected_month) | Q(date__month=prev_month)) &
        Q(Q(date__year = prev_year) | Q(date__year = prev_year)))
    
    roster_list = []
    for day in dates:
        att_dict = (day,'inactive')
        for record in records:
            if day == record.date:
                att_dict = (record.date, record.shift.color,)
                break
        roster_list.append(att_dict)

    shifts = Shift.objects.all()
    context = {
        "roster_list":roster_list,
        "shifts":shifts,
        "selected_year":selected_year,
        "selected_month":selected_month,
    }
    return render(request,"attendance-records/my-roster.html", context)

@login_required(login_url='login')
@permission_required(['attendance.view_attendancerecord', 'attendance.add_shift'], raise_exception=True)
def create_shift(request):
    if request.method == 'POST':
        form = CreateShiftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('roster')
    else:
        form = CreateShiftForm()

    context = {
        "form":form,
        }

    return render(request,"shifts/create-shift.html",context)