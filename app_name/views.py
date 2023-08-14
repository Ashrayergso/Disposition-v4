```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import Crew, Ship, Assignment, ShipSailingSchedule, PositionAndContractLength, ShipCrewAllowance, CertificateTypesAndExpiry
from .forms import CrewForm, ShipForm, AssignmentForm

def list_crew_members(request):
    crew = Crew.objects.all()
    return render(request, 'app_name/crew_list.html', {'crew': crew})

def crew_detail(request, pk):
    crew_member = get_object_or_404(Crew, pk=pk)
    return render(request, 'app_name/crew_detail.html', {'crew_member': crew_member})

def new_crew_member(request):
    if request.method == "POST":
        form = CrewForm(request.POST)
        if form.is_valid():
            crew_member = form.save(commit=False)
            crew_member.save()
            return redirect('crew_detail', pk=crew_member.pk)
    else:
        form = CrewForm()
    return render(request, 'app_name/crew_edit.html', {'form': form})

def edit_crew_member(request, pk):
    crew_member = get_object_or_404(Crew, pk=pk)
    if request.method == "POST":
        form = CrewForm(request.POST, instance=crew_member)
        if form.is_valid():
            crew_member = form.save(commit=False)
            crew_member.save()
            return redirect('crew_detail', pk=crew_member.pk)
    else:
        form = CrewForm(instance=crew_member)
    return render(request, 'app_name/crew_edit.html', {'form': form})

def list_ships(request):
    ships = Ship.objects.all()
    return render(request, 'app_name/ship_list.html', {'ships': ships})

def ship_detail(request, pk):
    ship = get_object_or_404(Ship, pk=pk)
    return render(request, 'app_name/ship_detail.html', {'ship': ship})

def new_ship(request):
    if request.method == "POST":
        form = ShipForm(request.POST)
        if form.is_valid():
            ship = form.save(commit=False)
            ship.save()
            return redirect('ship_detail', pk=ship.pk)
    else:
        form = ShipForm()
    return render(request, 'app_name/ship_edit.html', {'form': form})

def edit_ship(request, pk):
    ship = get_object_or_404(Ship, pk=pk)
    if request.method == "POST":
        form = ShipForm(request.POST, instance=ship)
        if form.is_valid():
            ship = form.save(commit=False)
            ship.save()
            return redirect('ship_detail', pk=ship.pk)
    else:
        form = ShipForm(instance=ship)
    return render(request, 'app_name/ship_edit.html', {'form': form})

def assign_crew_to_ship(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.save()
            return redirect('assignment_detail', pk=assignment.pk)
    else:
        form = AssignmentForm()
    return render(request, 'app_name/assignment_edit.html', {'form': form})
```