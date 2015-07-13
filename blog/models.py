from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
  user = models.ForeignKey(User)
  title = models.CharField(max_length = 50,blank = True,null = True)
  content = models.CharField(max_length = 300,blank = True,null = True)
  id1 = models.CharField(max_length = 10,default = '1',blank = True,null = True)
  def __unicode__ (self):
    return self.title