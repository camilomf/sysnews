from django.shortcuts import render
from django.apps import apps
from django.views.generic.base import TemplateView
from news.models import News, Country
from news.forms import NewsForm


# Create your views here.

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all()
        context['form_news'] = NewsForm
        context['latest_news'] = News.objects.all()[:5]
        return context