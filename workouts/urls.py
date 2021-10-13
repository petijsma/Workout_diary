from django.urls import path

from . import views

urlpatterns = [
    path("", views.WorkoutListView.as_view(), name="workout-list"),
    path("<int:pk>", views.WorkoutDetailView.as_view(), name="workout-detail"),
    path("contact", views.contact, name="contact"),
]