from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    author_fullname = models.CharField(max_length=100)
    title = models.CharField(max_length=50) # ----> yazi ucun limit var
    about = models.TextField()  #----> yazi ucun limit yoxdu
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author_fullname} --- {self.title}'
