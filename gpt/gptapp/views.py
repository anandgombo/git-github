# views.py
from django.shortcuts import render, redirect
from gptapp.models import CourtCase
from gptapp.form import CourtCaseForm

def case_list(request):
    cases = CourtCase.objects.all()
    return render(request, 'case_list.html', {'cases': cases})

def add_case(request):
    if request.method == 'POST':
        form = CourtCaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('case-list')
    else:
        form = CourtCaseForm()
    return render(request, 'add_case.html', {'form': form})

def update_case(request, pk):
    case = CourtCase.objects.get(pk=pk)
    if request.method == 'POST':
        form = CourtCaseForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('case-list')
    else:
        form = CourtCaseForm(instance=case)
    return render(request, 'update_case.html', {'form': form})

def delete_case(request, pk):
    case = CourtCase.objects.get(pk=pk)
    if request.method == 'POST':
        case.delete()
        return redirect('case-list')
    return render(request, 'delete_case.html', {'case': case})
def home(req):
    return render(req,'base.html')