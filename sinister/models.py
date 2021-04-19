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
  #  category =
    damage = models.TextField (max_length=500)
   # location ='''"""


    def __str__(self):
        return self.title