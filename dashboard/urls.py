
from django.urls import path
from .views import DashboardHomeView, NewsLetterDashboardHomeView
app_name="dashboard"

urlpatterns = [
  path('', DashboardHomeView.as_view(), name="home"),
  path('list/', NewsLetterDashboardHomeView.as_view(), name="list")
]
