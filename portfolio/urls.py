from django.urls import path
from portfolio import views

app_name = 'portfolio'

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]