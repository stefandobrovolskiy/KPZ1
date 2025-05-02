# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('articles/', views.ArticleList.as_view(), name='articles-list'),
    path('articles/<int:year>/<int:month>/<int:day>/<slug:slug>/', 
         views.ArticleDetail.as_view(), name='article-detail'),
]