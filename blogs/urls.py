from django.urls import path
from blogs import views as blog_views

urlpatterns = [
    path('', blog_views.all_blogs)
]