from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import NewsDetailView,NewsListView, CreateNews, DeleteNews, NewsUpdate, SourceCreate, TagsCreate, sourceList, sourceAdd
# from .views import HomePageView

news_patterns = ([
     path('', login_required(NewsListView.as_view()), name='news'),
     path('<int:pk>/<slug:slug>/', login_required(NewsDetailView.as_view()), name='detail'),
     path('update/<int:pk>', login_required(NewsUpdate.as_view()), name='update'),
     path('delete/<int:pk>', login_required(DeleteNews.as_view()), name='delete'),
     path('create/',  login_required(CreateNews.as_view()), name='create'),
     path('add_source',  login_required(SourceCreate.as_view()), name='add_source'),
     path('add_tags',  login_required(TagsCreate.as_view()), name='add_tags'),
     path('source_list', sourceList ),
     path('source_add', sourceAdd, name='source_add' ),
], 'news')
