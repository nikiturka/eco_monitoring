# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pollutant
from .forms import PollutantForm


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
