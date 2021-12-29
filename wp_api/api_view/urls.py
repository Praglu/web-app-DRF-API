from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("data-collector", views.ViewView.as_view(), name="view"),
    path("thank-you", views.thank_you, name="thank-you")
]
