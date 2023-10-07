from django.db import models
from django.contrib.auth.models import User
class recipe(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , blank=True)
    recipe_name = models.CharField(max_length=200)
    recipe_discription = models.TextField()
    recpie_image=models.ImageField(upload_to="recipe")
# Create your models here.
