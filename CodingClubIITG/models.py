from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.

class User(AbstractUser):
	IsApproved = models.BooleanField(default=False)

PROJECT_STATUS = (
    ("ongoing", "ongoing"),
    ("completed", "completed"),
)

class Projects(models.Model):
	name = models.CharField(max_length=1024)
	status = models.CharField(choices=PROJECT_STATUS, default='ongoing',max_length=1024)
	outline = models.CharField(max_length=500,blank=True,null=True)
	details = models.CharField(max_length=30000)
	prereq = models.CharField(max_length=1000,blank=True,null=True)
	date = models.DateField(default=date.today)
	img = models.ImageField(upload_to='projects/')

	def __str__(self):
		return self.name


# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=1024)
    venue = models.CharField(max_length=1024)
    speakers = models.CharField(max_length=1024)
    details = models.CharField(max_length=30000)
    date = models.DateField(default=date.today)
    img = models.FileField(upload_to='events/')

    def __str__(self):
            return self.name

class Members(models.Model):
	name= models.CharField(max_length=300)
	position=models.CharField(max_length=300)
	fblink=models.URLField(max_length=3000, blank=True, null=True)
	gitlink=models.URLField(max_length=3000, blank=True, null=True)
	intro=models.CharField(max_length=1000,blank=True,null=True)
	img= models.FileField(upload_to='members/')
	year = models.IntegerField()

	def __str__(self):
		return self.name

class Blog(models.Model):
	img = models.FileField(upload_to='blogs/')
	topic = models.CharField(max_length=1024)
	author = models.CharField(max_length=1024)
	posted_on = models.DateField(default=date.today)
	details = models.TextField()


# --------------------------------------------------------

# Favorites

class Favorite_events(models.Model):
	for_user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	event = models.ForeignKey(Event,on_delete=models.CASCADE)

class Favorite_projects(models.Model):
	for_user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	project = models.ForeignKey(Projects,on_delete=models.CASCADE)

# ------------------------------------------------------------

# Discussion Forum

class Discussion_events(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	event = models.ForeignKey(Event,on_delete=models.CASCADE)
	replied_to = models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True)
	text = models.TextField()

class Discussion_projects(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	project = models.ForeignKey(Projects,on_delete=models.CASCADE)
	replied_to = models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True)
	text = models.TextField()
# ---------------------------------------------------------------------------
