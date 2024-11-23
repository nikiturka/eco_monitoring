from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Pollutant, Enterprise, Record
from .forms import PollutantForm, EnterpriseForm, RecordForm


def home(request):
    return render(request, 'app/home.html')


class PollutantListView(ListView):
    model = Pollutant
    template_name = 'app/pollutant/pollutant_list.html'
    context_object_name = 'pollutants'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(pollutant_name__icontains=search_query)
        return queryset


class PollutantCreateView(CreateView):
    model = Pollutant
    form_class = PollutantForm
    success_url = reverse_lazy('pollutant_list')
    template_name = 'app/pollutant/pollutant_create.html'



class PollutantDetailView(DetailView):
    model = Pollutant
    template_name = 'app/pollutant/pollutant_detail.html'
    context_object_name = 'pollutant'


class PollutantUpdateView(UpdateView):
    model = Pollutant
    form_class = PollutantForm
    success_url = reverse_lazy('pollutant_list')
    template_name = 'app/pollutant/pollutant_update.html'


class PollutantDeleteView(DeleteView):
    model = Pollutant
    template_name = 'app/pollutant/pollutant_confirm_delete.html'
    success_url = reverse_lazy('pollutant_list')


class EnterpriseListView(ListView):
    model = Enterprise
    template_name = 'app/enterprise/enterprise_list.html'
    context_object_name = 'enterprises'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(enterprise_name__icontains=search_query)
        return queryset


class EnterpriseCreateView(CreateView):
    model = Enterprise
    form_class = EnterpriseForm
    success_url = reverse_lazy('enterprise_list')
    template_name = 'app/enterprise/enterprise_create.html'



class EnterpriseDetailView(DetailView):
    model = Enterprise
    template_name = 'app/enterprise/enterprise_detail.html'
    context_object_name = 'enterprise'


class EnterpriseUpdateView(UpdateView):
    model = Enterprise
    form_class = EnterpriseForm
    success_url = reverse_lazy('enterprise_list')
    template_name = 'app/enterprise/enterprise_update.html'


class EnterpriseDeleteView(DeleteView):
    model = Enterprise
    template_name = 'app/enterprise/enterprise_confirm_delete.html'
    success_url = reverse_lazy('enterprise_list')


class RecordListView(ListView):
    model = Record
    template_name = 'app/record/record_list.html'
    context_object_name = 'records'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(year__icontains=search_query) |
                Q(enterprise__enterprise_name__icontains=search_query) |
                Q(pollutant__pollutant_name__icontains=search_query) |
                Q(emission_per_year__icontains=search_query)
            )

        return queryset


class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    success_url = reverse_lazy('record_list')
    template_name = 'app/record/record_create.html'



class RecordDetailView(DetailView):
    model = Record
    template_name = 'app/record/record_detail.html'
    context_object_name = 'record'


class RecordUpdateView(UpdateView):
    model = Record
    form_class = RecordForm
    success_url = reverse_lazy('record_list')
    template_name = 'app/record/record_update.html'


class RecordDeleteView(DeleteView):
    model = Record
    template_name = 'app/record/record_confirm_delete.html'
    success_url = reverse_lazy('record_list')
