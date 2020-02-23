from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add= True)
    # add in  thumbnail later
    # add in  author later
    
    
    #To set default object information to display for articles
    def __str__(self):
        return self.title
    
    # To show only a snippet of the article
    def snippet(self):
        return self.body[:50] + '...'
        # Go to templates and invoke snippet instead of body
        