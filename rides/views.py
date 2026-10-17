from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from rides.models import Ride
from rides.forms import RideCreateForm, RideEditForm, RideDeleteForm

class RideListView(ListView):
    model = Ride
    template_name = 'rides/ride-list.html'
    context_object_name = 'rides'

class RideDetailView(DetailView):
    model = Ride
    template_name = 'rides/ride-details.html'
    context_object_name = 'ride'

class RideCreateView(CreateView):
    model = Ride
    form_class = RideCreateForm
    template_name = 'rides/ride-create.html'
    success_url = reverse_lazy('rides:ride-list')

class RideEditView(UpdateView):
    model = Ride
    form_class = RideEditForm
    template_name = 'rides/ride-edit.html'
    context_object_name = 'ride'

    def get_success_url(self):
        return reverse_lazy('rides:ride-details', kwargs={'pk': self.object.pk})



class RideDeleteView(DeleteView):
    model = Ride
    template_name = 'rides/ride-delete.html'
    success_url = reverse_lazy('rides:ride-list')
    context_object_name = 'ride'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RideDeleteForm(instance=self.object)

        return context
