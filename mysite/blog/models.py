# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models
from django.urls import reverse

class Category(models.Model):
    category = models.CharField(max_length=250, help_text='Максимум 250 символів')
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Категорія для публікацій'
        verbose_name_plural = 'Категорії для публікацій'

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        try:
            return reverse('articles-category-list', kwargs={'slug': self.slug})
        except:
            return "/"

class Article(models.Model):
    title = models.CharField(max_length=250, help_text='Максимум 250 символів')
    description = models.TextField(blank=True, verbose_name='Опис')
    pub_date = models.DateField(default=timezone.now, verbose_name='Дата публікації')
    slug = models.SlugField(unique_for_date='pub_date')
    main_page = models.BooleanField(default=True, help_text='Показувати на головній сторінці', verbose_name='Головна')
    category = models.ForeignKey(Category, related_name='articles', blank=True, null=True, 
                                verbose_name='Категорія', on_delete=models.CASCADE)
    objects = models.Manager()

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        try:
            return reverse('article-detail', kwargs={
                'year': self.pub_date.year,
                'month': self.pub_date.month,
                'day': self.pub_date.day,
                'slug': self.slug,
            })
        except:
            return "/"

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, verbose_name='Стаття', 
                                related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos', verbose_name='Фото')
    title = models.CharField(max_length=250, help_text='Максимум 250 символів', blank=True)

    class Meta:
        verbose_name = 'Фото для статті'
        verbose_name_plural = 'Фото для статті'

    def __str__(self):
        return self.title

    @property
    def filename(self):
        return self.image.name.rsplit('/', 1)[-1]
    
    # ТИМЧАСОВО, щоб не валився admin.py
class Post(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Пост (тимчасово)'
        verbose_name_plural = 'Пости (тимчасово)'

    def __str__(self):
        return self.title
