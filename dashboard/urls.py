
from django.urls import path
from .views import DashboardHomeView, NewsLetterDashboardHomeView, NewsLetterCreateView
app_name="dashboard"

urlpatterns = [
  path('', DashboardHomeView.as_view(), name="home"),
  path('list/', NewsLetterDashboardHomeView.as_view(), name="list"),
  path('create/', NewsLetterCreateView.as_view(), name="create")
]
