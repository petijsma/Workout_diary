from django.views.generic import ( ListView, DetailView,)
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.core.mail import send_mail

from .models import Workout

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