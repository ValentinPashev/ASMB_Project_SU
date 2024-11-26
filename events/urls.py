from django.urls import path, include
from events.views import CreateEventView, DashboardView, EventDetailsView, EditEventView, DeleteEventView

urlpatterns = [
    path('', CreateEventView.as_view(), name='create_event'),
    path('dashboard/', DashboardView.as_view(), name='dash'),
    path('<int:pk>/', include([
        path('event-details/', EventDetailsView.as_view(), name='event_details'),
        path('edit-event/', EditEventView.as_view(), name='edit_event'),
        path('delete-event/', DeleteEventView.as_view(), name='delete_event'),
    ])),
]