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
from django.http import HttpResponse, JsonResponse
import json
from django.core import serializers

# Create your views here.
class HomePageView(ListView):
    queryset = News.objects.all()
    template_name = "core/home.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all().order_by('name')
        context['tags_list'] = Tags.objects.all()
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

def is_valid_queryparam(param):
    return param != '' and param is not None and len(param) > 0

def formatDate(date):
    nd = date.split('/')
    mm = nd [0]
    dd = nd [1]
    yy = nd [2]
    return str(yy+"-"+mm+"-"+dd)

def searchFilter(request):
    qs = News.objects.all()
    title_contains_query = request.GET.get('title_contains')
    daterange_query = request.GET.get('daterange')
    country_query = request.GET.getlist('countries')
    tags_query = request.GET.getlist('tags')

    if is_valid_queryparam(tags_query):
        print ("tags")
        qs = qs.filter(tags__in=tags_query)

    if is_valid_queryparam(title_contains_query):
        print ("title")
        qs = qs.filter(title__icontains=title_contains_query)

    if is_valid_queryparam(daterange_query):
        print ("daTE")
        daterange_query = daterange_query.split(' - ')
        daterange_query[0] = formatDate(daterange_query[0])
        daterange_query[1] = formatDate(daterange_query[1])
        qs = qs.filter(publication_date__range=[daterange_query[0],daterange_query[1]])

    if is_valid_queryparam(country_query):
        print ("country")
        print (country_query)
        qs = qs.filter(country__in=country_query)

    context = {
        'list_news' : qs
    }
    return render(request,"core/home.html",context)

@login_required
def countryList(request):
    countries = Country.objects.all()
    countries = [ countrySerializer(country) for country in countries ]
    return HttpResponse(json.dumps(countries),content_type='application/json')

def countrySerializer(country):
    return {'id':country.id,'name':country.name}




# @login_required
# def searchByCountry(request, id):
#     # id=Country.objects.filter(name=q)
#     news = News.objects.filter(country=id)
#     # context = {}
#     context = context_permanent(news)
#     # context['news_list'] = news
#     # context['countries'] = Country.objects.all()
#     # context['editors'] = User.objects.filter(groups=2)
#     return render(request, 'core/home.html', context)


# @login_required
# def searchByTags(request, **kwargs):
#     tags = request.POST.getlist('search_by_tags')
#     print (tags)
#     # context = {}
#     # context['countries'] = Country.objects.all()
#     # context['tags'] = Tags.objects.all()
#     if len(tags) == 1:
#         print ("1")
#         news = News.objects.filter(tags=tags[0])    
#         context = context_permanent(news)
#         return render(request, 'core/home.html', context)
#     if len(tags) == 2:
#         print ("2")
#         news = News.objects.filter(Q(tags__id__icontains=tags[0]) and Q(tags__id__icontains=tags[1]))
#         print (news)
#         context = context_permanent(news)
#         return render(request, 'core/home.html', context)
#     if len(tags) == 3:
#         print ("3")
#         news = News.objects.filter(Q(tags__id__icontains=tags[0]) and Q(tags__id__icontains=tags[1]) and Q(tags__id__contains=tags[2]))
#         print (news)
#         context = context_permanent(news)
#         return render(request, 'core/home.html', context)
    
# @login_required
# def searchByUser(request, **kwargs):
#     q = request.POST.get('search_by_user')
#     news = News.objects.filter(editor=q).order_by('-created')
#     context = context_permanent(news)
#     # context = {}
#     # context['news_list'] = news
#     # context['countries'] = Country.objects.all()
#     return render(request, 'core/home.html', context)

# def context_permanent(news):
#     context = {}
#     context['list_news'] = news
#     context['countries'] = Country.objects.all()
#     context['tags'] = Tags.objects.all()
#     context['users'] = User.objects.filter(groups=2)
#     return context