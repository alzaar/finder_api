from django.urls import path
from .views import FinderView

urlpatterns = [path("", FinderView.as_view())]
