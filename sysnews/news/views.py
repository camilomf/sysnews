from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import View
from django.http import JsonResponse
from .models import News
from .forms import NewsForm

# Create your views here.

class NewsDetailView(DetailView):
    model = News

class NewsListView(ListView):
    model = News

class CreateNews(CreateView):
    form_class = NewsForm
    # template_name = 'noticia/noticia_list.html'
 
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.editor = self.request.user
        instance.save()
        # messages.success(request, "Successfully Created")
        return redirect('home')

class DeleteNews(DeleteView):
    model = News
    success_url = reverse_lazy('home')    