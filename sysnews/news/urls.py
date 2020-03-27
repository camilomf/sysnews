from django.urls import path
from .views import NewsDetailView,NewsListView, CreateNews, DeleteNews
# from .views import HomePageView

news_patterns = ([
     path('', NewsListView.as_view(), name='news'),
     path('<int:pk>/<slug:slug>/', NewsDetailView.as_view(), name='detail'),
     path('<int:pk>', DeleteNews.as_view(), name='delete'),
     path('create/',  CreateNews.as_view(), name='create'),
], 'news')