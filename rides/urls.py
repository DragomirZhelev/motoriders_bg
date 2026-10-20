from django.urls import path

from rides import views
from rides.views import RideListView, RideDetailView, RideCreateView, RideEditView, RideDeleteView, \
    RideReviewCreateView, RideReviewListView, RideReviewEditView, RideReviewDeleteView, RideReviewDetailView

app_name = 'rides'
urlpatterns = [
    path('list/', RideListView.as_view(), name='ride-list'),

    path('details/<int:pk>/', RideDetailView.as_view(), name='ride-details'),

    path('create/', RideCreateView.as_view(), name='ride-create'),

    path('edit/<int:pk>/', RideEditView.as_view(), name='ride-edit'),

    path('delete/<int:pk>/', RideDeleteView.as_view(), name='ride-delete'),

    path('ride-review/create/', RideReviewCreateView.as_view(), name='ride-review-create'),

    path('ride-review/list/', RideReviewListView.as_view(), name='ride-review-list'),

    path('ride-review/edit/<int:pk>/', RideReviewEditView.as_view(), name='ride-review-edit'),

    path('ride-review/delete/<int:pk>/', RideReviewDeleteView.as_view(), name='ride-review-delete'),

    path('ride-review/details/<int:pk>/', RideReviewDetailView.as_view(), name='ride-review-details'),


    path('join/<int:pk>/', views.join_ride, name='join-ride'),

    path('leave/<int:pk>/<int:rider_pk>/', views.leave_ride, name='leave-ride'),


]