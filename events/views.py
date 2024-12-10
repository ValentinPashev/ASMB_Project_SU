from django.contrib.auth import get_user_model
from django.forms import modelform_factory
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView, DetailView, UpdateView, DeleteView
from accounts.models import Profile
from events.forms import CreateEventForm, SearchForm, CommentFormSet, DeleteEventForm, EventReportForm
from events.models import Event, EventReport


# Create your views here.

class CreateEventView(CreateView):
    model = Event
    form_class = CreateEventForm
    template_name = 'events/create-event-template.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.created_by = self.request.user.email
        return super().form_valid(form)


class DashboardView(ListView, FormView):
    template_name = 'events/dashboard.html'
    context_object_name = 'events'
    form_class = SearchForm
    paginate_by = 8
    model = Event
    success_url = reverse_lazy('dash')

    def get_queryset(self):
        queryset = self.model.objects.all()
        print(self.request.user.get_user_permissions())


        if 'events.can_approve_events' not in self.request.user.get_group_permissions() or not self.request.user.has_perm('events.can_approve_events'):
            queryset = queryset.filter(approved=True,)

        queryset = queryset.filter(completed=False)

        if 'query' in self.request.GET:
            query = self.request.GET.get('query')
            queryset = self.queryset.filter(title__icontains=query)

        return queryset


def approve_event(request, pk):
    event = Event.objects.get(pk=pk)
    event.approved = True
    event.save()

    return redirect(request.META.get('HTTP_REFERER'))

class EventDetailsView(DetailView):
    model = Event
    template_name = 'events/event-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = CommentFormSet()
        return context

    def post(self, request, *args, **kwargs):
        event = self.get_object()
        formset = CommentFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.event = event
                    comment.save()

            return redirect('event_details', pk=event.id)

        context = self.get_context_data(**kwargs)
        context['formset'] = formset

        return self.render_to_response(context)


class EditEventView(UpdateView):
    model = Event
    template_name = 'events/edit-event.html'
    success_url = reverse_lazy('dash')

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Event, fields='__all__')

        else:
            return modelform_factory(Event, fields=('date', 'description'))


class DeleteEventView(DeleteView, FormView):
    model = Event
    template_name = 'events/delete-event.html'
    form_class = DeleteEventForm
    success_url = reverse_lazy('dash')

    def dispatch(self, request, *args, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg)
        event = self.get_object()
        profile = self.request.user.profile

        if event.created_by != profile.__str__() and not self.request.user.is_superuser:
            return HttpResponseForbidden("You do not have permission to delete this event.")

        return super().dispatch(request, *args, **kwargs)



    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        event = Event.objects.get(pk=pk)
        return event.__dict__


def pass_event_report(request, pk):
    event = get_object_or_404(Event, pk=pk)
    print(request.user.get_user_permissions())

    if event.created_by != request.user.email:
        return HttpResponseForbidden("This event was created by another user.")

    if request.method == 'POST':
        form = EventReportForm(request.POST)
        if form.is_valid():
            event_report = form.save(commit=False)
            event_report.event = event
            event_report.save()
            distribute_points_from_event(event_report, pk)
            return redirect('index')

        context = {'form': form, 'event': event}
    else:
        form = EventReportForm()
        context = {'form': form, 'event': event}

    return render(request, 'events/event_report.html', context)


def distribute_points_from_event(event_report, pk):
    if not isinstance(event_report, EventReport):
        raise ValueError("The event_report must be a Event instance.")

    if event_report.completed:
        raise ValueError("The event_report is already completed.")

    User = get_user_model()
    organizers = event_report.organizers.split(', ')
    list_with_user_points = []

    for email in organizers:
        try:
            user = User.objects.get(email=email)
            profile = Profile.objects.get(user=user)
            if user not in list_with_user_points:
                profile.points_from_events += event_report.points_for_organizers
                profile.save()
                list_with_user_points.append(user)

        except User.DoesNotExist:
            print(f"User with email {email} does not exist. Check for errors!")


    event_report.completed = True
    event_report.save()
    event = Event.objects.get(pk=pk)
    event.completed = True
    event.save()


# class EventReportDashBoardView(ListView):
#     template_name = 'event_reports/dashboard.html'
#     context_object_name = 'event_reports'
#     paginate_by = 8
#     model = EventReport
#     success_url = reverse_lazy('dash')
#
#     def get_queryset(self):
#         queryset = self.model.objects.all()
#

#to be continued!!!