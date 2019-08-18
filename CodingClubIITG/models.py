from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Projects(models.Model):
	name = models.CharField(max_length=1024)
	status = models.BooleanField(default=True)
	outline = models.CharField(max_length=500)
	details = models.CharField(max_length=30000)
	prereq = models.CharField(max_length=1000)
	date = models.DateField(default=date.today)

	def __str__(self):
		return self.name
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
