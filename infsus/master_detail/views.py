from django.shortcuts import render, redirect
from .forms import ComputerForm, DeskForm, ComputerComponentForm, ComputerComponentFormSet
from .models import Computer, Desk, ComputerComponent


def computer_list(request):
    computers = Computer.objects.all()
    return render(request, 'master_detail/computer_list.html', {'computers': computers})

def computer_add(request):
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('computer_list')
    else:
        form = ComputerForm()
    return render(request, 'master_detail/computer_form.html', {'form': form})

def computer_edit(request, pk):
    computer = Computer.objects.get(pk=pk)
    if request.method == 'POST':
        form = ComputerForm(request.POST, instance=computer)
        formset = ComputerComponentFormSet(request.POST, instance=computer)
        if form.is_valid():
            form.save()
            return redirect('computer_list')
    else:
        form = ComputerForm(instance=computer)
        formset = ComputerComponentFormSet(request.POST, instance=computer)
    return render(request, 'master_detail/computer_edit.html', {'form': form, 'formset': formset, 'computer': computer})

def computer_delete(request, pk):
    computer = Computer.objects.get(pk=pk)
    computer.delete()
    return redirect('computer_list')

def desk_list(request):
    desks = Desk.objects.all()
    return render(request, 'master_detail/desk_list.html', {'desks': desks})

def desk_add(request):
    if request.method == 'POST':
        form = DeskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('desk_list')
    else:
        form = DeskForm()
    return render(request, 'master_detail/desk_form.html', {'form': form})

def desk_edit(request, pk):
    desk = Desk.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeskForm(request.POST, instance=desk)
        if form.is_valid():
            form.save()
            return redirect('desk_list')
    else:
        form = DeskForm(instance=desk)
    return render(request, 'master_detail/desk_form.html', {'form': form})

def desk_delete(request, pk):
    desk = Desk.objects.get(pk=pk)
    desk.delete()
    return redirect('desk_list')

def component_create(request, pk):
    computer = Computer.objects.get(pk=pk)
    if request.method == 'POST':
        form = ComputerComponentForm(request.POST)
        if form.is_valid():
            component = form.save(commit=False)
            component.computer = computer
            component.save()
            return redirect('computer_edit', pk)
    else:
        form = ComputerComponentForm()
    return render(request, 'master_detail/component_create.html', {'form': form, 'computer': computer})

def component_edit(request, pk):
    component = ComputerComponent.objects.get(pk=pk)
    computer = component.computer
    if request.method == 'POST':
        form = ComputerComponentForm(request.POST, instance=component)
        if form.is_valid():
            form.save()
            return redirect('computer_edit', computer.pk)
    else:
        form = ComputerComponentForm(instance=component)
    return render(request, 'master_detail/component_edit.html', {'form': form, 'component': component, 'computer': computer})

def component_delete(request, pk):
    component = ComputerComponent.objects.get(pk=pk)
    computer_pk = component.computer.pk
    component.delete()
    return redirect('computer_edit', computer_pk)
