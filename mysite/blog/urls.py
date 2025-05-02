# blog/urls.py
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('articles/', views.ArticleList.as_view(), name='articles-list'),
    path('articles/category/<slug:slug>/', views.ArticleCategoryList.as_view(), name='articles-category-list'),
    re_path(r'^articles/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$', 
            views.ArticleDetail.as_view(), name='article-detail'),
]