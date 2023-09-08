from django.db import models
from django.urls import reverse

#model for pages table in database with title, content, author, and date fields
class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('get_page', args=[str(self.id)])