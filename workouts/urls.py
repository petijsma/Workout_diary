from django.urls import path

from . import views

urlpatterns = [
    path("", views.WorkoutListView.as_view(), name="workout-list"),
    path("<int:pk>", views.WorkoutDetailView.as_view(), name="workout-detail"),
    path("contact", views.contact, name="contact"),
    path("create", views.WorkoutCreateView.as_view(), name="workout-create"),
    path("<int:pk>/update", views.WorkoutUpdateView.as_view(), name="workout-update"),
    path("<int:pk>/delete", views.WorkoutDeleteView.as_view(), name="workout-delete"),
]