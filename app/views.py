from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Pollutant, Enterprise, Record, Tax, Risk
from .forms import PollutantForm, EnterpriseForm, RecordForm, TaxForm, RiskForm
from .services import TaxCalculatorFactory, RiskCalculatorFactory


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


class TaxCreateView(CreateView):
    model = Tax
    form_class = TaxForm
    template_name = 'app/tax/tax_create.html'
    success_url = reverse_lazy('tax_create')

    def form_valid(self, form):
        record = form.cleaned_data['record']
        tax_type = form.cleaned_data['tax_type']

        tax = Tax.objects.filter(record=record, tax_type=tax_type).first()

        if not tax:
            tax_calculator = TaxCalculatorFactory.get_calculator(tax_type)
            tax_amount = tax_calculator(record)

            tax = form.save(commit=False)
            tax.tax_amount = tax_amount
            tax.save()

        context = self.get_context_data(
            form=form,
            tax=tax,
            tax_type=tax_type,
            tax_amount=tax.tax_amount,
            emission_per_year=tax.record.emission_per_year,
            pollutant_tax_value=tax.pollutant_tax_type_value,
            pollutant=record.pollutant
        )

        return self.render_to_response(context)


class RiskCreateView(CreateView):
    model = Risk
    form_class = RiskForm
    template_name = 'app/risk/risk_create.html'
    success_url = reverse_lazy('risk_create')

    def form_valid(self, form):
        pollutant = form.cleaned_data['pollutant']
        risk = Risk.objects.filter(pollutant=pollutant).first()
        risk_calculator = RiskCalculatorFactory.get_calculator(risk.substance_type)

        current_risk = risk_calculator(risk)

        risk.current_risk = current_risk
        risk.save()

        context = self.get_context_data(
            form=form,
            pollutant=pollutant,
            current_risk=current_risk,
            concentration=risk.concentration,
            rfc=risk.rfc
        )

        return self.render_to_response(context)
