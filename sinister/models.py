from django.db import models

# Create your models here.
Sinister_type = (
    ('incendie','incendie'),
    ('accident','accident'),
)

class Sinister(models.Model):
    title = models.CharField(max_length=100)
    sister_type = models.CharField(max_length=20,choices= Sinister_type )
    description = models.TextField(max_length=500)
    published_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    damage = models.TextField (max_length=500)
   # location ='''"""


    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name