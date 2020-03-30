from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import View
from django.http import JsonResponse
from .models import News
from .forms import NewsForm, SourceForm, TagsForm
from django.utils.text import slugify

# Create your views here.

class NewsDetailView(DetailView):
    model = News

class NewsListView(ListView):
    model = News

class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/news_create.html'
 
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.editor = self.request.user
        instance.save()
        form.save_m2m()
        # messages.success(request, "Successfully Created")
        return redirect('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_source'] = SourceForm
        context['form_tags'] = TagsForm
        return context

class NewsUpdate(UpdateView):
    model = News
    form_class = NewsForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        news = get_object_or_404(News, pk=self.kwargs['pk'])
        return reverse("news:detail", args=(news.id,slugify(news.title)))

class DeleteNews(DeleteView):
    model = News
    success_url = reverse_lazy('home')    

### Source

class SourceCreate (CreateView):
    form_class = SourceForm
    success_url = reverse_lazy('news:create')    
    # template_name = 'news/news_create.html'
 
### Tags

class TagsCreate (CreateView):
    form_class = TagsForm
    success_url = reverse_lazy('news:create')    
    # template_name = 'news/news_create.html'