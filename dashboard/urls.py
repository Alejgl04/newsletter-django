
from django.urls import path
from .views import DashboardHomeView, NewsLetterDashboardHomeView, NewsLetterCreateView, NewsLetterDetailView
app_name="dashboard"

urlpatterns = [
  path('', DashboardHomeView.as_view(), name="home"),
  path('list/', NewsLetterDashboardHomeView.as_view(), name="list"),
  path('create/', NewsLetterCreateView.as_view(), name="create"),
  path('detail/<int:pk>', NewsLetterDetailView.as_view(), name="detail")
]
