from django.urls import path
from accounts import views as account_views
urlpatterns = [
    path('say-hi/', account_views.say_hi)
]