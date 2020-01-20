from django.conf import settings
from django.db import models
from django.utils import timezone

class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published_date__lte=timezone.now())

class Post(models.Model):
    #プロパティ author～published_dateまで
    # models.ForeignKey　他のモデルへのリンク
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # models.CharField　文字数が制限されたテキストを定義するフィールド
    title = models.CharField(max_length=200)
    # models.TextField　文字数制限なしの長いテキスト用フィールド
    text = models.TextField()
    # models.DateTimeField　日付と時間のフィールド
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    objects = PostQuerySet.as_manager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
