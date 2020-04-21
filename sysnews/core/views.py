from django.shortcuts import render
from django.apps import apps
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from news.models import News, Country, Tags
from news.forms import NewsForm
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.models import Group, User

# Create your views here.

class HomePageView(ListView):
    queryset = News.objects.all()
    template_name = "core/home.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all().order_by('name')
        context['tags'] = Tags.objects.all()
        context['users'] = User.objects.filter(groups=2)
        list_news = News.objects.all()
        paginator = Paginator(list_news, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)

        # context = context_permanent(None)
        context['list_news'] = file_exams
        return context

@login_required
def searchByTitle(request, **kwargs):
    q = request.POST.get('search_by_title')
    news = News.objects.filter(Q(title__icontains=q)).order_by('-created')
    # news = News.objects.filter(title__search=q)
    # context = {}
    context = context_permanent(news)
    # context['news_list'] = news
    # context['countries'] = Country.objects.all()
    # context['editors'] = User.objects.filter(groups=2)
    return render(request, 'core/home.html', context)

@login_required
def searchByCountry(request, id):
    # id=Country.objects.filter(name=q)
    news = News.objects.filter(country=id)
    # context = {}
    context = context_permanent(news)
    # context['news_list'] = news
    # context['countries'] = Country.objects.all()
    # context['editors'] = User.objects.filter(groups=2)
    return render(request, 'core/home.html', context)

@login_required
def searchByDate(request, **kwargs):
    q = request.POST.get('search_by_date')
    news = News.objects.filter(Q(publication_date__icontains=q)).order_by('-created')
    context = context_permanent(news)
    # context = {}
    # context['news_list'] = news
    # context['countries'] = Country.objects.all()
    return render(request, 'core/home.html', context)

@login_required
def searchByTags(request, **kwargs):
    tags = request.POST.getlist('search_by_tags')
    # context = {}
    # context['countries'] = Country.objects.all()
    # context['tags'] = Tags.objects.all()
    if len(tags) == 1:
        news = News.objects.filter(tags=tags[0])
        context = context_permanent(news)
        return render(request, 'core/home.html', context)
    if len(tags) == 2:
        news = News.objects.filter(Q(tags__id__icontains=tags[0]) & Q(tags__id__icontains=tags[1]))
        context = context_permanent(news)
        return render(request, 'core/home.html', context)
    if len(tags) == 3:
        news = News.objects.filter(Q(tags__id__icontains=tags[0]) & Q(tags__id__icontains=tags[1]) & Q(tags__id__contains=tags[2]))
        context = context_permanent(news)
        return render(request, 'core/home.html', context)
    
@login_required
def searchByUser(request, **kwargs):
    q = request.POST.get('search_by_user')
    news = News.objects.filter(editor=q).order_by('-created')
    context = context_permanent(news)
    # context = {}
    # context['news_list'] = news
    # context['countries'] = Country.objects.all()
    return render(request, 'core/home.html', context)

def context_permanent(news):
    context = {}
    context['list_news'] = news
    context['countries'] = Country.objects.all()
    context['tags'] = Tags.objects.all()
    context['users'] = User.objects.filter(groups=2)
    return context