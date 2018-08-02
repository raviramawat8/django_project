from django.db import models

# Create your models here.
class signup(models.Model):
    UserName = models.CharField(max_length=100,unique=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    Phoneno = models.IntegerField(default=0)
    def __str__(self):
        return "{}".format(self.UserName)
