from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    post_username = models.CharField(max_length=50,null=True,blank=False)
    title = models.CharField(max_length=100,unique=True,blank=False,null=True)
    desc = models.TextField(max_length=300,blank=False)
    date_created = models.DateTimeField(auto_now_add=True,null=True,blank=False)
    date_updated = models.DateTimeField(auto_now=True,null=True,blank=False)
    parent_post = models.IntegerField(null=True,blank=False)


    def __str__(self):
        return self.title
        
    

