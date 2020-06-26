from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import HomePageView
from . import views

urlpatterns = [
    path('', login_required(HomePageView.as_view()), name="home"),
    path('search', login_required(views.searchFilter), name="search"),
    # path('search_by_user/',views.searchByUser, name="search_by_user"),
    # path('search_by_tags/',views.searchByTags, name="search_by_tags"),
    path('country/',views.countryList, name="country_list"),
    path('tag_by_country/',views.tagByCountry, name="tag_by_country"),
]