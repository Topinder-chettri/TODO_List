from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True) 
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")


   
