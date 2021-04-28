from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	address = models.CharField(max_length = 200, default ='')
	image = models.ImageField(upload_to='Profile_pics')