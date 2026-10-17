from django.urls import path

from riders.views import RiderListView, RiderDetailView, RiderCreateView, RiderDeleteView, RiderEditView

app_name = 'riders'
urlpatterns = [
    path('list/', RiderListView.as_view(), name='rider-list'),

    path('details/<int:pk>/', RiderDetailView.as_view(), name='rider-details'),

    path('create/', RiderCreateView.as_view(), name='rider-create'),

    path('delete/<int:pk>/', RiderDeleteView.as_view(), name='rider-delete'),

    path('edit/<int:pk>/', RiderEditView.as_view(), name='rider-edit'),


]