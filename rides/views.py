from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from rides.models import Ride, RideReview
from rides.forms import RideCreateForm, RideEditForm, RideDeleteForm, RideReviewCreateForm, RideReviewEditForm, RideReviewDeleteForm

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

class RideReviewDetailView(DetailView):
    model = RideReview
    template_name = 'rides/ride-review-details.html'
    context_object_name = 'ride_review'



class RideReviewListView(ListView):
    model = RideReview
    template_name = 'rides/ride-review-list.html'
    context_object_name = 'ride_reviews'


class RideReviewCreateView(CreateView):
    model = RideReview
    form_class = RideReviewCreateForm
    template_name = 'rides/ride-review-create.html'
    success_url = reverse_lazy('rides:ride-review-list')

class RideReviewEditView(UpdateView):
    model = RideReview
    form_class = RideReviewEditForm
    template_name = 'rides/ride-review-edit.html'
    context_object_name = 'ride_review'

    def get_success_url(self):
        return reverse_lazy('rides:ride-review-details', kwargs={'pk': self.object.pk})


class RideReviewDeleteView(DeleteView):
    model = RideReview
    template_name = 'rides/ride-review-delete.html'
    context_object_name = 'ride_review'
    success_url = reverse_lazy('rides:ride-review-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = RideReviewDeleteForm(instance=self.object)

        return context


