from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import NewsDetailView,NewsListView, CreateNews, DeleteNews, NewsUpdate, SourceCreate, TagsCreate
# from .views import HomePageView

news_patterns = ([
     path('', login_required(NewsListView.as_view()), name='news'),
     path('<int:pk>/<slug:slug>/', login_required(NewsDetailView.as_view()), name='detail'),
     path('update/<int:pk>', login_required(NewsUpdate.as_view()), name='update'),
     path('delete/<int:pk>', login_required(DeleteNews.as_view()), name='delete'),
     path('create/',  login_required(CreateNews.as_view()), name='create'),
     path('source/add/',  login_required(SourceCreate.as_view()), name='add_source'),
     path('tags/add/',  login_required(TagsCreate.as_view()), name='add_tags'),
], 'news')
