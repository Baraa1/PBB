# Django Classes
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
#My Classes
from .forms import *
from .models import *
from .filters import *
from ProjectManager.decorators import *
from .decorators import *


################################################################################################################################################################################
############################################################################# Terminals ########################################################################################
################################################################################################################################################################################

@login_required(login_url='login')
@user_passes_test(view_terminals)
def terminals(request):
    terminals       = Terminal.objects.all()
    terminal_filter = TerminalFilter(request.GET, Terminal.objects.filter().distinct())

    # if the user issued a filter request return the filtered data
    if request.method == "POST":
        terminal_filter = TerminalFilter(request.POST, Terminal.objects.filter().distinct())
        context         = {"terminals": terminal_filter.qs}
        return render(request,'tables/terminals-table.html', context)
    # else return all users data
    context = {
        "terminals":terminals,
        "terminal_filter":terminal_filter
        }

    return render(request,"terminals.html",context)

@login_required(login_url='login')
@user_passes_test(view_terminals)
def search_terminals(request):
    search_field  = request.POST.get('search-radios')
    record_filter = filter_terminals(request.POST.get('search-bar'), search_field)
    context       = {"terminals": record_filter}

    return render(request,'tables/terminals-table.html', context)

@login_required(login_url='login')
@user_passes_test(add_terminals)
def create_terminal(request):
    if request.method == 'POST':
        form = CreateTerminalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('terminals')
    else:
        form = CreateTerminalForm()

    context = {
        "form":form,
        }

    return render(request,"create-terminal.html",context)

@login_required(login_url='login')
@user_passes_test(update_terminals)
def update_terminal(request, pk):
    terminal = get_object_or_404(Terminal, id = pk)

    if request.method == 'POST':
        form = UpdateTerminalForm(request.POST,instance=terminal)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.info(request, f'{terminal.terminal_name} was successfully edited')
            return redirect('terminals')
    else:
        form = UpdateTerminalForm(instance=terminal)
    
    context = {
        'form': form,
        # sending the id for the delete
        'terminalid':terminal.id
    }

    return render(request, 'update-terminal.html', context)

@login_required(login_url='login')
@user_passes_test(delete_terminals)
def delete_terminal(request,pk):
    terminal = get_object_or_404(Terminal, id = pk)
    terminal.delete()
    messages.success(request, f'{terminal.terminal_name} and all records related to it were deleted, Good Job!')
    return redirect('terminals')

################################################################################################################################################################################
############################################################################# GATES ############################################################################################
################################################################################################################################################################################

@login_required(login_url='login')
@user_passes_test(view_gates)
def gates(request):
    gates = Gate.objects.all()
    gate_filter = GateFilter(request.GET, Gate.objects.filter().distinct())

    # if the user issued a filter request return the filtered data
    if request.method == "POST":
        gate_filter = GateFilter(request.POST, Gate.objects.filter().distinct())
        context = {
            "gates": gate_filter.qs,
            }
        return render(request,'tables/gates-table.html', context)
    # else return all gates data
    context = {
        "gates":gates,
        "gate_filter":gate_filter
        }

    return render(request,"gates.html",context)

@login_required(login_url='login')
@user_passes_test(view_gates)
def search_gates(request):
    search_field = request.POST.get('search-radios')
    record_filter = filter_gates(request.POST.get('search-bar'), search_field)
    context = {
        "gates": record_filter,
        }
    return render(request,'tables/gates-table.html', context)

@login_required(login_url='login')
@user_passes_test(add_gates)
def create_gate(request):
    if request.method == 'POST':
        form = CreateGateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gates')
    else:
        form = CreateGateForm()

    context = {
        "form":form,
        }

    return render(request,"create-gate.html",context)

@login_required(login_url='login')
@user_passes_test(update_gates)
def update_gate(request, pk):
    gate = get_object_or_404(Gate, id = pk)

    if request.method == 'POST':
        form = UpdateGateForm(request.POST,instance=gate)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.info(request, f'{gate.gate_name} was successfully edited')
            return redirect('gates')
    else:
        form = UpdateGateForm(instance=gate)
    
    context = {
        'form': form,
        # sending the id for the delete
        'gateid':gate.id
    }

    return render(request, 'update-gate.html', context)

@login_required(login_url='login')
@user_passes_test(delete_gates)
def delete_gate(request,pk):
    gate = get_object_or_404(Gate, id = pk)
    gate.delete()
    messages.success(request, f'{gate.gate_name} and all records related to it were deleted!')
    return redirect('gates')

################################################################################################################################################################################
############################################################################# STANDS ###########################################################################################
################################################################################################################################################################################

@login_required(login_url='login')
@user_passes_test(view_stands)
def stands(request):
    stands = Stand.objects.all()
    stand_filter = StandFilter(request.GET, Stand.objects.filter().distinct())

    # if the user issued a filter request return the filtered data
    if request.method == "POST":
        stand_filter = StandFilter(request.POST, Stand.objects.filter().distinct())
        context = {
            "stands": stand_filter.qs,
            }
        return render(request,'tables/stands-table.html', context)
    # else return all stands data
    context = {
        "stands":stands,
        "stand_filter":stand_filter
        }

    return render(request,"stands.html",context)

@login_required(login_url='login')
@user_passes_test(view_stands)
def search_stands(request):
    search_field = request.POST.get('search-radios')
    record_filter = filter_stands(request.POST.get('search-bar'), search_field)
    context = {
        "stands": record_filter,
        }
    return render(request,'tables/stands-table.html', context)

@login_required(login_url='login')
@user_passes_test(add_stands)
def create_stand(request):
    if request.method == 'POST':
        form = CreateStandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stands')
    else:
        form = CreateStandForm()

    context = {
        "form":form,
        }

    return render(request,"create-stand.html",context)

@login_required(login_url='login')
@user_passes_test(update_stands)
def update_stand(request, pk):
    stand = get_object_or_404(Stand, id = pk)

    if request.method == 'POST':
        form = UpdateStandForm(request.POST,instance=stand)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.info(request, f'{stand.stand_name} was successfully edited')
            return redirect('stands')
    else:
        form = UpdateStandForm(instance=stand)
    
    context = {
        'form': form,
        # sending the id for the delete
        'standid':stand.id
    }

    return render(request, 'update-stand.html', context)

@login_required(login_url='login')
@user_passes_test(delete_stands)
def delete_stand(request,pk):
    stand = get_object_or_404(Stand, id = pk)
    stand.delete()
    messages.success(request, f'{stand.stand_name} and all records related to it were deleted!')
    return redirect('stands')

################################################################################################################################################################################
############################################################################# PBBs #############################################################################################
################################################################################################################################################################################

@login_required(login_url='login')
@user_passes_test(view_pbbs)
def pbbs(request):
    pbbs = Pbb.objects.all()
    pbb_filter = PbbFilter(request.GET, Pbb.objects.filter().distinct())

    # if the user issued a filter request return the filtered data
    if request.method == "POST":
        pbb_filter = PbbFilter(request.POST, Pbb.objects.filter().distinct())
        context = {
            "pbbs": pbb_filter.qs,
            }
        return render(request,'tables/pbbs-table.html', context)
    # else return all pbbs data
    context = {
        "pbbs":pbbs,
        "pbb_filter":pbb_filter
        }

    return render(request,"pbbs.html",context)

@login_required(login_url='login')
@user_passes_test(view_pbbs)
def search_pbbs(request):
    search_field = request.POST.get('search-radios')
    record_filter = filter_pbbs(request.POST.get('search-bar'), search_field)
    context = {
        "pbbs": record_filter,
        }
    return render(request,'tables/pbbs-table.html', context)

@login_required(login_url='login')
@user_passes_test(add_pbbs)
def create_pbb(request):
    if request.method == 'POST':
        form = CreatePbbForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pbbs')
    else:
        form = CreatePbbForm()

    context = {
        "form":form,
        }

    return render(request,"create-pbb.html",context)

@login_required(login_url='login')
@user_passes_test(update_pbbs)
def update_pbb(request, pk):
    pbb = get_object_or_404(Pbb, id = pk)

    if request.method == 'POST':
        form = UpdatePbbForm(request.POST,instance=pbb)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.info(request, f'{pbb.pbb_name} was successfully edited')
            return redirect('pbbs')
    else:
        form = UpdatePbbForm(instance=pbb)
    
    context = {
        'form': form,
        # sending the id for the delete
        'pbbid':pbb.id
    }

    return render(request, 'update-pbb.html', context)

@login_required(login_url='login')
@user_passes_test(delete_pbbs)
def delete_pbb(request,pk):
    pbb = get_object_or_404(Pbb, id = pk)
    pbb.delete()
    messages.success(request, f'{pbb.pbb_name} and all records related to it were deleted!')
    return redirect('pbbs')