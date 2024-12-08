from django.forms import modelform_factory
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView, DetailView, UpdateView, DeleteView
from events.forms import CreateEventForm, SearchForm, CommentFormSet, DeleteEventForm
from events.models import Event


# Create your views here.

class CreateEventView(CreateView):
    model = Event
    form_class = CreateEventForm
    template_name = 'events/create-event-template.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.created_by = self.request.user.profile
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
            queryset = queryset.filter(approved=True)

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

#
# def example_view(request):
#     user = request.user
#     current_user_profile = user.profile.first_name
#     print(current_user_profile)