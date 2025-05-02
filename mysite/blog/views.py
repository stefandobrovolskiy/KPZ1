from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DateDetailView
from .models import Article, Category

class HomePageView(ListView):
    model = Category
    template_name = 'blog/index.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(main_page=True)[:3]
        return context

class ArticleDetail(DateDetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'item'
    date_field = 'pub_date'
    query_pk_and_slug = True
    month_format = '%m'
    allow_future = True

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        try:
            context['images'] = context['item'].images.all()
        except:
            pass
        return context

class ArticleList(ListView):
    model = Article
    template_name = 'blog/articles_list.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category_slug = self.request.GET.get('category')
        if category_slug:
            try:
                context['category'] = Category.objects.get(slug=category_slug)
            except Category.DoesNotExist:
                context['category'] = None
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = Article.objects.select_related('category').all()
        category_slug = self.request.GET.get('category')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset

class ArticleCategoryList(ArticleList):
    def get_queryset(self, *args, **kwargs):
        return Article.objects.filter(category__slug=self.kwargs['slug']).select_related('category').distinct()