# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pollutant, Enterprise
from .forms import PollutantForm, EnterpriseForm


def pollutant_list_create(request):
    if request.method == "POST":
        form = PollutantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pollutant_list_create')
    else:
        form = PollutantForm()

    pollutants = Pollutant.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        pollutants = pollutants.filter(pollutant_name__icontains=search_query)

    context = {
        'pollutants': pollutants,
        'form': form,
    }
    return render(request, 'app/pollutant_list_create.html', context)


def pollutant_retrieve_update_delete(request, id):
    pollutant = get_object_or_404(Pollutant, id=id)

    if request.method == "POST":
        form = PollutantForm(request.POST, instance=pollutant)
        if form.is_valid():
            form.save()
            return redirect('pollutant_list_create')
    elif request.method == "DELETE":
        pollutant.delete()
        return redirect('pollutant_list_create')
    else:
        form = PollutantForm(instance=pollutant)

    context = {
        'pollutant': pollutant,
        'form': form,
    }
    return render(request, 'app/pollutant_retrieve_update_delete.html', context)


def enterprise_list_create(request):
    if request.method == "POST":
        form = EnterpriseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enterprise_list_create')
    else:
        form = EnterpriseForm()

    enterprises = Enterprise.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        enterprises = enterprises.filter(enterprise_name__icontains=search_query)

    context = {
        'enterprises': enterprises,
        'form': form,
    }
    return render(request, 'app/enterprise_list_create.html', context)


def enterprise_retrieve_update_delete(request, id):
    enterprise = get_object_or_404(Enterprise, id=id)

    if request.method == "POST":
        form = EnterpriseForm(request.POST, instance=enterprise)
        if form.is_valid():
            form.save()
            return redirect('enterprise_list_create')
    elif request.method == "DELETE":
        enterprise.delete()
        return redirect('enterprise_list_create')
    else:
        form = EnterpriseForm(instance=enterprise)

    context = {
        'enterprise': enterprise,
        'form': form,
    }
    return render(request, 'app/enterprise_retrieve_update_delete.html', context)
