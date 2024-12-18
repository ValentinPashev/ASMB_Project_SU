from django.urls import path, include
from events.views import CreateEventView, DashboardView, EventDetailsView, EditEventView, DeleteEventView, \
    approve_event, pass_event_report, EventReportListView, EventReportDetailView, EventReportUpdateView

urlpatterns = [
    path('', CreateEventView.as_view(), name='create_event'),
    path('dashboard/', DashboardView.as_view(), name='dash'),
    path('dash-reports/', EventReportListView.as_view(), name='dash_reports'),
    path('reports/<int:pk>/', EventReportDetailView.as_view(), name='event-report-detail'),
    path('reports/<int:pk>/edit/', EventReportUpdateView.as_view(), name='event-report-update'),
    path('<int:pk>/', include([
        path('event-details/', EventDetailsView.as_view(), name='event_details'),
        path('edit-event/', EditEventView.as_view(), name='edit_event'),
        path('delete-event/', DeleteEventView.as_view(), name='delete_event'),
        path('approve/', approve_event, name='approve'),
        path('report/', pass_event_report, name='pass_event_report'),



    ])),
]