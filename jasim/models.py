from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Profile(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    bio = models.TextField()
    profession = models.CharField(max_length=100)
    age = models.CharField(max_length=4)
    gender = models.CharField(max_length=10)
    skills = models.CharField(max_length=200)


class Project(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="projects")
    title = models.CharField(max_length=100)
    description = models.TextField()
    photos = models.ImageField(null= True, upload_to='screenshots')
    created_on = models.DateField()
    duration = models.CharField(max_length=100)
    client_website = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    client_email = models.CharField(max_length=100)
    project_url = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, related_name="reviews")
    client = models.CharField(max_length=100)
    review_description = models.TextField()
    added_on = models.DateTimeField(default = timezone.now)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return self.review_description

