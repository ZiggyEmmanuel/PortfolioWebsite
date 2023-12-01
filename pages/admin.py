from django.contrib import admin
from portfolio.models import Project
from pages.models import Home, About, Services, SocialMedia, CV

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    pass

class PagesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Home, PagesAdmin)
admin.site.register(SocialMedia)
admin.site.register(CV)
admin.site.register(About)
admin.site.register(Services)