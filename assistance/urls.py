from django.urls import path

from assistance.views import HelpRequestListView, HelpRequestDetailView, HelpRequestCreateView, HelpRequestEditView, \
    HelpRequestDeleteView

app_name = 'assistance'
urlpatterns = [
    path('list/', HelpRequestListView.as_view(), name='help-request-list'),

    path('details/<int:pk>/', HelpRequestDetailView.as_view(), name='help-request-details'),

    path('create/', HelpRequestCreateView.as_view(), name='help-request-create'),

    path('edit/<int:pk>', HelpRequestEditView.as_view(), name='help-request-edit'),

    path('delete/<int:pk>', HelpRequestDeleteView.as_view(), name='help-request-delete'),



]