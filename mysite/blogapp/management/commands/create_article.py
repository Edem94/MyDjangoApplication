from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction
from typing import Sequence
from blogapp.models import Article, Category, Author, Tag


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Create new article")
        author = Author.objects.get(name="Arsen Popov")
        category = Category.objects.get(name="Sport")
        tags: Sequence[Tag] = Tag.objects.filter(name='sport')
        article, created = Article.objects.get_or_create(
            title="Breaking news #3!",
            author=author,
            category=category,
        )
        for tag in tags:
            article.tags.add(tag)
        self.stdout.write(f"Created article {article}")
