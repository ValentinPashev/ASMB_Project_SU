from django.contrib import messages
from django.contrib.auth import get_user_model
from django.forms import modelform_factory
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView, DetailView, UpdateView, DeleteView
from accounts.models import Profile
from events.forms import CreateEventForm, SearchForm, CommentFormSet, DeleteEventForm, EventReportForm
from events.models import Event, EventReport
from students.models import ActivityLog
from django.utils.timezone import now


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

    if not request.user.can_make_reports and event.created_by != request.user.email:
        return HttpResponseForbidden("This event was created by another user.")

    if request.method == 'POST':
        form = EventReportForm(request.POST)
        if form.is_valid():
            event_report = form.save(commit=False)
            event_report.event = event
            event_report.save()
            distribute_points_from_event(request, event_report, pk)
            return redirect('index')

        context = {'form': form, 'event': event}
    else:
        form = EventReportForm()
        context = {'form': form, 'event': event}

    return render(request, 'events/event_report.html', context)


def distribute_points_from_event(request, event_report, pk):
    event = get_object_or_404(Event, pk=pk)

    if not isinstance(event_report, EventReport):
        messages.error(request, "The event_report must be an Event instance.")
        return

    if event_report.completed:
        messages.error(request, "The event_report is already completed.")
        return

    User = get_user_model()
    roles_and_points = {
        "organizers": event_report.points_for_organizers,
        "prepared": event_report.points_for_prepared,
        "participated_actively": event_report.points_for_participated_actively,
        "attended": event_report.points_for_attended,
    }
    list_with_user_points = []
    emails_do_no_exist = []

    for role, points in roles_and_points.items():
        emails = getattr(event_report, role).split(' ')
        for email in emails:
            try:
                user = User.objects.get(email=email)
                profile = Profile.objects.get(user=user)
                if user not in list_with_user_points:
                    profile.points_from_events += points
                    profile.save()


                    ActivityLog.objects.create(
                        profile=profile,
                        message=f"Присъствал на {event.name}, като {role} ----> {points} точки.",
                        timestamp=now()
                    )

                    list_with_user_points.append(user)
                    messages.success(request, f"Точки добавени за {email} ({role}): {points} точки.")
            except User.DoesNotExist:
                emails_do_no_exist.append(email)

    if emails_do_no_exist:
        messages.error(request, f"Съответните имейли {[e for e in emails_do_no_exist]} не бяха намерени!")

    event_report.completed = True
    event_report.save()
    event.completed = True
    event.save()

    messages.success(request, f"Разпределението на точките за събитието {event.name} е завършено успешно.")


