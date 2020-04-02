from django.shortcuts import render
from django.apps import apps
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from news.models import News, Country
from news.forms import NewsForm
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger



# Create your views here.

class HomePageView(ListView):
    queryset = News.objects.all()
    template_name = "core/home.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all()
        list_news = News.objects.all()
        paginator = Paginator(list_news, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)

        context['list_news'] = file_exams
        return context
        # context['latest_news'] = News.objects.all()
        # # context['latest_news'] = News.objects.order_by('-created')[:5]

        # result_list = sorted(
        #     chain(result_list, form_news, latest_news),
        #     key=attrgetter('entry_date'),
        #     reverse=True)
