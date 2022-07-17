from django.db import models

# Create your models here.
class UserModel(models.Model):
    dummy_text = models.CharField(max_length=255, blank=True)
    text_number = models.IntegerField()

    def __str__(self):
        return self.dummy_text