from django.db import models

# Create your models here.

# HOME SECTION

class Home(models.Model):
    Name = models.CharField(max_length=25)
    Greetings = models.CharField(max_length=20)
    Home_Copy = models.TextField(blank=True)
    Picture = models.ImageField(upload_to="picture/")
    # save time when home page info is modified
    Updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

class SocialMedia(models.Model):
    social_media = models.ForeignKey(Home,
                                   on_delete=models.CASCADE)
    Social_Name = models.CharField(max_length=15, blank=True)
    Socialmedia_Url = models.URLField(max_length=200, blank=True)
    Social_Icon = models.CharField(max_length=45, blank=True)

    def __str__(self):
        return self.Social_Name

#CV UPLOAD

class CV(models.Model):
    Title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to="cv_pdf/")

    def __str__(self):
        return self.Title

# ABOUT SECTION

class About(models.Model):
    Heading = models.CharField(max_length=30)
    Career = models.CharField(max_length=50)
    Description = models.TextField(blank=False)
    Profile_img = models.ImageField(upload_to="profile/")
    # save time when home page info is modified
    Updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Heading

class Profile(models.Model):
    about_page = models.ForeignKey(About,
                                   on_delete=models.CASCADE)
    Social_name = models.CharField(max_length=10)
    links = models.URLField(max_length=200)

# SERVICES SECTION

class Services(models.Model):
    Service_Name = models.CharField(max_length=40)
    Icon = models.CharField(max_length=40)

    # save time when service page info is modified
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.Service_Name

class Category(models.Model):
    services = models.ForeignKey(Services,
                                   on_delete=models.CASCADE)
    category_name = models.CharField(max_length=30)