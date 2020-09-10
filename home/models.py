from django.db import models 

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=500)
    date = models.DateField()
 
    def __str__(self):
        return self.name
 
class Image(models.Model):
    image = models.ImageField(upload_to='pic')
 

 