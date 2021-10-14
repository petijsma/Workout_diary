from django.views.generic import ( ListView, DetailView, CreateView, UpdateView, DeleteView,)
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Workout

class LockedView(LoginRequiredMixin):
    login_url = "admin:login"
class WorkoutListView(ListView):
    model = Workout
    queryset = Workout.objects.all().order_by("-date_of_workout")

class WorkoutDetailView(DetailView):
    model = Workout

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name, # subject
            message, # message
            message_email, # from
            ['petijsma@gmail.com'] # to
        )

        return render(request, 'workouts/contact.html', {'message_name': message_name})
    else:
        return render(request, 'workouts/contact.html', {})

class WorkoutCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Workout
    fields = ["title", "content", "date_of_workout"]
    success_url = reverse_lazy("workout-list")
    success_message = "You added new entry!"

class WorkoutUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Workout
    fields = ["title", "content", "date_of_workout"]
    success_message = "Your entry was updated!"

    def get_success_url(self):
        return reverse_lazy("workout-list")
class WorkoutDeleteView(LockedView, DeleteView):
    model = Workout
    success_url = reverse_lazy("workout-list")
    success_message = "Your entry was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)