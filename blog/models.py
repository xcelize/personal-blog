from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save
from froala_editor.fields import FroalaField
from tinymce.models import HTMLField


class Article(models.Model):

    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=254)
    image = models.ImageField(upload_to='images/')
    content = HTMLField()
    slug = models.SlugField(max_length=100,unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'article'
        get_latest_by = 'created_at'

    def __str__(self):
        return "{0}".format(self.title)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Comment(models.Model):

    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'commentaire'


class Category(models.Model):

    label = models.CharField(max_length=100)

    def __str__(self):
        return "{0}".format(self.label)

    class Meta:
        verbose_name = 'categorie'


class Tag(models.Model):

    label = models.CharField(max_length=100)

    def __str__(self):
        return "{0}".format(self.label)


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    exists = Article.objects.filter(slug=slug).exists()
    instance.slug = slug



pre_save.connect(pre_save_post_receiver, sender=Article)