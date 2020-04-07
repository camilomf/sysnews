from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import HomePageView
from . import views

urlpatterns = [
    path('', login_required(HomePageView.as_view()), name="home"),
    path('search_by_title/',views.searchByTitle, name="search_by_title"),
    path('search_by_date/',views.searchByDate, name="search_by_date"),
    path('<id>/',views.searchByCountry, name="search_by_country"),
]