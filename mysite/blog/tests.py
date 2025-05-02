from django.test import TestCase
from django.urls import reverse
from .models import Article, Category
from django.utils import timezone

class BlogTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category="Тест", slug="test")
        self.article = Article.objects.create(
            title="Тестова стаття",
            slug="test-article",
            pub_date=timezone.now(),
            description="Тестовий вміст",
            category=self.category,
            main_page=True
        )

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, self.category.category)

    def test_articles_list(self):
        response = self.client.get(reverse('articles-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles_list.html')
        self.assertContains(response, self.article.title)

    def test_article_detail(self):
        response = self.client.get(reverse('article-detail', kwargs={
            'year': self.article.pub_date.year,
            'month': self.article.pub_date.month,
            'day': self.article.pub_date.day,
            'slug': self.article.slug
        }))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article_detail.html')
        self.assertContains(response, self.article.title)