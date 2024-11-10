# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pollutant, Enterprise, Record
from .forms import PollutantForm, EnterpriseForm, RecordForm


def home(request):
    return render(request, 'app/home.html')


def pollutant_list_create(request):
    search_query = request.GET.get('q')
    pollutants = Pollutant.objects.all()
    if search_query:
        pollutants = pollutants.filter(pollutant_name__icontains=search_query)

    if request.method == "POST":
        form = PollutantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pollutant_list_create')
    else:
        form = PollutantForm()

    context = {
        'entities': pollutants,
        'form': form,
        'entity_name': 'Забруднювачів',
        'entity_list_url': 'pollutant_list_create',
        'entity_retrieve_update_delete_url': 'pollutant_retrieve_update_delete',
        'request': request,
    }
    return render(request, 'app/base_list_create.html', context)


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
        'entity': pollutant,
        'form': form,
        'entity_name': 'Забруднювач',
        'entity_list_url': 'pollutant_list_create',
        'entity_retrieve_update_delete_url': 'pollutant_retrieve_update_delete',
    }
    return render(request, 'app/base_retrieve_update_delete.html', context)


def enterprise_list_create(request):
    search_query = request.GET.get('q')
    enterprises = Enterprise.objects.all()
    if search_query:
        enterprises = enterprises.filter(enterprise_name__icontains=search_query)

    if request.method == "POST":
        form = EnterpriseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enterprise_list_create')
    else:
        form = EnterpriseForm()

    context = {
        'entities': enterprises,
        'form': form,
        'entity_name': 'Підприємств',
        'entity_list_url': 'enterprise_list_create',
        'entity_retrieve_update_delete_url': 'enterprise_retrieve_update_delete',
        'request': request,
    }
    return render(request, 'app/base_list_create.html', context)


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
        'entity': enterprise,
        'form': form,
        'entity_name': 'Підприємство',
        'entity_list_url': 'enterprise_list_create',
        'entity_retrieve_update_delete_url': 'enterprise_retrieve_update_delete',
    }
    return render(request, 'app/base_retrieve_update_delete.html', context)


def record_list_create(request):
    search_query = request.GET.get('q')
    records = Record.objects.all()
    if search_query:
        records = records.filter(enterprise__enterprise_name__icontains=search_query)

    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_list_create')
    else:
        form = RecordForm()

    context = {
        'entities': records,
        'form': form,
        'entity_name': 'Записи',
        'entity_list_url': 'record_list_create',
        'entity_retrieve_update_delete_url': 'record_retrieve_update_delete',
        'request': request,
    }
    return render(request, 'app/base_list_create.html', context)


def record_retrieve_update_delete(request, id):
    record = get_object_or_404(Record, id=id)

    if request.method == "POST":
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record_list_create')
    elif request.method == "DELETE":
        record.delete()
        return redirect('record_list_create')
    else:
        form = RecordForm(instance=record)

    context = {
        'entity': record,
        'form': form,
        'entity_name': 'Запис',
        'entity_list_url': 'record_list_create',
        'entity_retrieve_update_delete_url': 'record_retrieve_update_delete',
    }
    return render(request, 'app/base_retrieve_update_delete.html', context)
