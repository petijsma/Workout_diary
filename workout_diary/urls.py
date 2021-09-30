from django.urls import path

from . import views

urlpatterns = [
    path("workouts", views.WorkoutListView.as_view(), name="workout-list"),
    path("workouts/<int:pk>", views.WorkoutDetailView.as_view(), name="workout-detail"),
    path("workouts/contact", views.contact, name="contact"),
]