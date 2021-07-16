from django.db import models

# Create your models here.
class Post(models.Model):
    time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    url = models.URLField(default='youtube.com/c/txtdrustadz')
    description = models.TextField()

    def __str__(self):
        return "{}.{}".format(self.id,self.title)