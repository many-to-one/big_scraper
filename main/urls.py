from django.urls import path
from .views import StartScraperView

urlpatterns = [
    path('scrape/', StartScraperView.as_view(), name='scrape'),
]