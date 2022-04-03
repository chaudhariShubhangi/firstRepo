
from django.urls import path

from App1.views import testing

urlpatterns = [
    path('test/',testing)
]