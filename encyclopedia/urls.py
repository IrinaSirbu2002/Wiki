from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.entry, name="entry"),
    path("new/", views.new, name="new"),
    path("edit/", views.edit, name="edit"),
    path("random/", views.random_entry, name="random")
]
