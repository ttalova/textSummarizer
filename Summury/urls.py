from django.urls import path
from .views import MethodView

urlpatterns = [
    path("", MethodView.as_view(), name="method"),
]