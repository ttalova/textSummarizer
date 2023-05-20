from django.urls import path
from .views import MethodView

urlpatterns = [
    path("<int:id>", MethodView.as_view(), name="method"),
]