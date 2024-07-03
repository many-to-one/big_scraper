from django.urls import path
from .views import getScraper

urlpatterns = [
    path('scrape/', getScraper.as_view(), name='scrape'),
]