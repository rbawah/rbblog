import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Category(models.Model):
    """Model representing the Category of the post."""
    name = models.CharField(max_length=100,
                            help_text='Enter the Topic (e.g. Blog, Tutorial, etc)')
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category-posts', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Topic(models.Model):
    """Model representing the topic being discussed."""
    name = models.CharField(max_length=100,
                            help_text='Enter the Topic (e.g. Python, Machine Learning, Algorithms, etc)')
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:topic-articles', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be 2 characters or more.")]
    )
    summary = models.TextField(
        null=True, blank=True,
    )
    serial_num = models.FloatField(
        null=True, blank=True,
    )
    #text = models.TextField(
        #validators=[MinLengthValidator(2, "Body must be 2 characters or more.")]
    text = RichTextUploadingField(
            validators=[MinLengthValidator(2, "Body must be 2 characters or more.")],
            external_plugin_resources=[(
                'youtube',
                '/static/ckeditor/plugins/youtube/youtube/',
                'plugin.js',
            )],
    )

    published_date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    topics = models.ManyToManyField(Topic)
    category = models.ManyToManyField(Category)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        ordering = ['id']

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

