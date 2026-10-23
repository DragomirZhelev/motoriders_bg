from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from riders.models import Rider
# Create your views here.
from rides.models import Ride, RideReview
from rides.forms import RideCreateForm, RideEditForm, RideDeleteForm, RideReviewCreateForm, RideReviewEditForm, RideReviewDeleteForm, JoinRideForm
from django.views.decorators.http import require_POST



class RideListView(ListView):
    model = Ride
    template_name = 'rides/ride-list.html'
    context_object_name = 'rides'

    def get_queryset(self):
        queryset = super().get_queryset()

        search_query = self.request.GET.get('search')
        status = self.request.GET.get('status')
        sort = self.request.GET.get('sort')

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(ride_organizer__first_name__icontains=search_query) |
                Q(ride_organizer__last_name__icontains=search_query) |
                Q(ride_organizer__nickname__icontains=search_query) |
                Q(participants__first_name__icontains=search_query) |
                Q(participants__last_name__icontains=search_query) |
                Q(participants__nickname__icontains=search_query) |
                Q(meeting_point__icontains=search_query) |
                Q(destination__icontains=search_query) |
                Q(road_types__icontains=search_query) |
                Q(road_difficulty__icontains=search_query) |
                Q(description__icontains=search_query)
            ).distinct()
        if status:
            queryset = queryset.filter(status=status)

        if sort == 'latest':
            queryset = queryset.order_by('-created_at')

        elif sort == 'oldest':
            queryset = queryset.order_by('created_at')

        return queryset

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

    def get_queryset(self):
        queryset = super().get_queryset()

        search_query = self.request.GET.get('search')

        if search_query:
            queryset = queryset.filter(
                Q(ride__title__icontains=search_query) |
                Q(reviewer__first_name__icontains=search_query) |
                Q(reviewer__last_name__icontains=search_query) |
                Q(reviewer__nickname__icontains=search_query)
            )

        return queryset



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


def join_ride(request, pk):
    ride = get_object_or_404(Ride, pk=pk)

    if request.method == 'POST':
        form = JoinRideForm(request.POST)
        if form.is_valid():
            rider = form.cleaned_data['rider']


            if ride.status != 'Planned':
                form.add_error(None, 'You can join only Rides in status Planned')

            elif ride.participants.count() >= ride.maximum_riders_to_join:
                form.add_error(None, 'Number of maximum riders for this ride has been reached already')

            elif rider == ride.ride_organizer:
                # raise ValidationError('The organizer of the ride can not join the participants list')
                form.add_error('rider', 'The organizer of the ride shall not join as participant')
            elif rider in ride.participants.all():
                form.add_error('rider', 'This rider is already part of the participants list')
            else:
                ride.participants.add(rider)

                return redirect('rides:ride-details', pk=ride.pk)

    else:
        form = JoinRideForm()

    context = {'ride': ride, 'form': form,}

    return render(request, 'rides/ride-join.html', context)


@require_POST
def leave_ride(request, pk, rider_pk):
    ride = get_object_or_404(Ride, pk=pk)
    rider = get_object_or_404(Rider, pk=rider_pk)

    status_ride = ride.status

    if status_ride == 'Planned':
        if rider in ride.participants.all():
            ride.participants.remove(rider)

    return redirect('rides:ride-details', pk=pk)
