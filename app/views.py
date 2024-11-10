# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pollutant, Enterprise, Record
from .forms import PollutantForm, EnterpriseForm, RecordForm


def get_list_create_context(request, entity_list, form, entity_name, list_url, retrieve_update_delete_url):
    search_query = request.GET.get('q')
    if search_query:
        entity_list = entity_list.filter(pollutant_name__icontains=search_query)

    context = {
        'entities': entity_list,
        'form': form,
        'entity_name': entity_name,
        'entity_list_url': list_url,
        'entity_retrieve_update_delete_url': retrieve_update_delete_url,
        'request': request,
    }
    return context


def get_retrieve_update_destroy_context(request, entity, form, entity_name, list_url, retrieve_update_delete_url):
    context = {
        'entity': entity,
        'form': form,
        'entity_name': entity_name,
        'entity_list_url': list_url,
        'entity_retrieve_update_delete_url': retrieve_update_delete_url,
    }
    return context


def pollutant_list_create(request):
    if request.method == "POST":
        form = PollutantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pollutant_list_create')
    else:
        form = PollutantForm()

    pollutants = Pollutant.objects.all()

    context = get_list_create_context(
        request,
        pollutants,
        form,
        'Забруднювач',
        'pollutant_list_create',
        'pollutant_retrieve_update_delete'
    )
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

    context = get_retrieve_update_destroy_context(
        request,
        pollutant,
        form,
        'Забруднювач',
        'pollutant_list_create',
        'pollutant_retrieve_update_delete'
    )
    return render(request, 'app/base_retrieve_update_delete.html', context)


def enterprise_list_create(request):
    if request.method == "POST":
        form = EnterpriseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enterprise_list_create')
    else:
        form = EnterpriseForm()

    enterprises = Enterprise.objects.all()

    context = get_list_create_context(
        request,
        enterprises,
        form,
        'Підприємство',
        'enterprise_list_create',
        'enterprise_retrieve_update_delete'
    )
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

    context = get_retrieve_update_destroy_context(
        request,
        enterprise,
        form,
        'Підприємство',
        'enterprise_list_create',
        'enterprise_retrieve_update_delete'
    )
    return render(request, 'app/base_retrieve_update_delete.html', context)


def record_list_create(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_list_create')
    else:
        form = RecordForm()

    records = Record.objects.all()

    context = get_list_create_context(
        request,
        records,
        form,
        'Запис',
        'record_list_create',
        'record_retrieve_update_delete'
    )
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

    context = get_retrieve_update_destroy_context(
        request,
        record,
        form,
        'Запис',
        'record_list_create',
        'record_retrieve_update_delete'
    )
    return render(request, 'app/base_retrieve_update_delete.html', context)
