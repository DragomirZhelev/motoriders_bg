from django.urls import path

from rides.views import RideListView, RideDetailView, RideCreateView, RideEditView, RideDeleteView

app_name = 'rides'
urlpatterns = [
    path('list/', RideListView.as_view(), name='ride-list'),

    path('details/<int:pk>/', RideDetailView.as_view(), name='ride-details'),

    path('create/', RideCreateView.as_view(), name='ride-create'),

    path('edit/<int:pk>/', RideEditView.as_view(), name='ride-edit'),

    path('delete/<int:pk>/', RideDeleteView.as_view(), name='ride-delete'),



]