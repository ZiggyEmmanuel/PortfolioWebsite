from django.db import models

# Create your models here.

class Project(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Technology = models.CharField(max_length=50)
    Image = models.ImageField(upload_to="portfolio_images/", blank=True)
    
    def __str__(self):
        return self.Title