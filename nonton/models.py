from django.db import models
from django.utils.text import slugify
# Create your models here.
class Post(models.Model):
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField()
    playlist = models.CharField(max_length=225)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return "{}.{}".format(self.id,self.title)