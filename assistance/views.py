from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from assistance.models import Rider, HelpRequest
from assistance.forms import HelpRequestCreateForm, HelpRequestEditForm, HelpRequestDeleteForm

# Create your views here.
class HelpRequestListView(ListView):
    model = HelpRequest
    template_name = 'assistance/help-request-list.html'
    context_object_name = 'help_requests'

class HelpRequestDetailView(DetailView):
    model = HelpRequest
    template_name = 'assistance/help-request-details.html'
    context_object_name = 'help_request'


class HelpRequestCreateView(CreateView):
    model = HelpRequest
    form_class = HelpRequestCreateForm
    template_name = 'assistance/help-request-create.html'
    success_url = reverse_lazy('assistance:help-request-list')

class HelpRequestEditView(UpdateView):
    model = HelpRequest
    form_class = HelpRequestEditForm
    template_name = 'assistance/help-request-edit.html'
    context_object_name = 'help_request'

    def get_success_url(self):
        return reverse_lazy('assistance:help-request-details', kwargs={'pk': self.object.pk})


class HelpRequestDeleteView(DeleteView):
    model = HelpRequest
    template_name = 'assistance/help-request-delete.html'
    context_object_name = 'help_request'
    success_url = reverse_lazy('assistance:help-request-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = HelpRequestDeleteForm(instance=self.object)

        return context


