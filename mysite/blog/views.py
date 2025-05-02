from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DateDetailView, DetailView
from .models import Article, Category

class HomePageView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(main_page=True)[:3]
        return context

    def get_queryset(self):
        return Category.objects.all()

class ArticleList(ListView):
    model = Article
    template_name = 'blog/articles_list.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['category'] = Category.objects.get(slug=self.kwargs.get('slug'))
        except:
            context['category'] = None
        return context

class ArticleCategoryList(ArticleList):
    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['slug']).distinct()

class ArticleDetail(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        return context