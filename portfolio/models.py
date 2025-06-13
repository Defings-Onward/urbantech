from django.db import models

class Project(models.Model):
    pic = models.ImageField(upload_to='images')
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    date  = models.DateField(auto_now_add=True)
    git_url = models.URLField()
    project_url = models.URLField()
    note = models.TextField()
    substance = models.CharField(max_length=200)

class Media(models.Model):
    image = models.ImageField(upload_to='images')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    type = models.CharField(max_length=200, default="image")



# Create your models here.
