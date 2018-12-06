from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe
from djrichtextfield.models import RichTextField
from markdown import markdown


class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(allow_unicode=True, unique=True)
    keyword = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True, unique=True)
    keyword = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    excerpt = models.TextField()
    content = RichTextField()
    image = models.ImageField(blank=True,
                              null=True,
                              height_field="height_field",
                              width_field="width_field",
                              upload_to='media')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ["-timestamp", "-updated"]

    def __str__(self):
        return self.title

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))


