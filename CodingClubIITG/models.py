from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

    def publish(self):
        self.created_on = timezone.now()
        self.save()

def modulo(num, val):
    return num % val
