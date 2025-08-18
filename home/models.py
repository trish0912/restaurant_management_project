from django.db import models

# Create your models here.
class Feedback(models.Model):
    comments = models.TextField()

    def __str__(self):
        return f"Feedback - {self.comments[:30]}..."