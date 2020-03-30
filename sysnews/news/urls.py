from django.urls import path
from .views import NewsDetailView,NewsListView, CreateNews, DeleteNews, NewsUpdate, SourceCreate, TagsCreate
# from .views import HomePageView

news_patterns = ([
     path('', NewsListView.as_view(), name='news'),
     path('<int:pk>/<slug:slug>/', NewsDetailView.as_view(), name='detail'),
     path('update/<int:pk>', NewsUpdate.as_view(), name='update'),
     path('delete/<int:pk>', DeleteNews.as_view(), name='delete'),
     path('create/',  CreateNews.as_view(), name='create'),
     path('source/add/',  SourceCreate.as_view(), name='add_source'),
     path('tags/add/',  TagsCreate.as_view(), name='add_tags'),
], 'news')
