from django.db.models import Q
from django.shortcuts import render
from riders.models import Rider
from riders.forms import RiderCreateForm, RiderEditForm, RiderDeleteForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class RiderListView(ListView):
    model = Rider
    template_name = 'riders/rider-list.html'
    context_object_name = 'riders'

    def get_queryset(self):
        queryset = super().get_queryset()

        search_query = self.request.GET.get('search')

        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(nickname__icontains=search_query)
            )

        return queryset

class RiderDetailView(DetailView):
    model = Rider
    template_name = 'riders/rider-details.html'
    context_object_name = 'rider'


class RiderCreateView(CreateView):
    model = Rider
    form_class = RiderCreateForm
    template_name = 'riders/rider-create.html'
    success_url = reverse_lazy('riders:rider-list')

class RiderDeleteView(DeleteView):
    model = Rider
    template_name = 'riders/rider-delete.html'
    success_url = reverse_lazy('riders:rider-list')
    context_object_name = 'rider'


    #check get_initial - ?
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = RiderDeleteForm(instance=self.object)

        return context

class RiderEditView(UpdateView):
    model = Rider
    form_class = RiderEditForm
    template_name = 'riders/rider-edit.html'
    context_object_name = 'rider'

    def get_success_url(self):
        return reverse_lazy('riders:rider-details', kwargs={'pk': self.object.pk})
