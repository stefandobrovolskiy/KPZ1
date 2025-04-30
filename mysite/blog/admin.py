# -*- coding: utf-8 -*-
from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import Article, ArticleImage, Category
from .forms import ArticleImageForm

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')
    prepopulated_fields = {'slug': ('category',)}
    fieldsets = (
        (None, {
            'fields': ('category', 'slug'),
        }),
    )

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0
    fieldsets = (
        (None, {
            'fields': ('title', 'image',),
        }),
    )

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'category', 'main_page')
    list_filter = ('pub_date', 'category')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'pub_date'
    ordering = ('pub_date',)
    inlines = [ArticleImageInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'pub_date', 'category', 'main_page'),
        }),
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)