from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction
from typing import Sequence
from blogapp.models import Article, Category, Author, Tag


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Selecting article fields")
        articles: Sequence[Article] = Article.objects.defer('content').all()
        for article in articles:
            print(f"Article title: {article.title}; "
                  f"author: {article.author.name}; "
                  f"category: {article.category.name}; "
                  f"published: {article.pub_date}"
                  )
            for tag in article.tags.all():
                print(f'tag: {tag.name}')

        self.stdout.write("Done")
