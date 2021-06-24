from django.urls import path
from django.views.generic import TemplateView

app_name = 'keci'

urlpatterns = [
    path('',TemplateView.as_view(template_name="keci/index.html")),
]