from django.db import models

# Create your models here.
class Feedback(models.Model):
    comments = models.TextField()

    def __str__(self):
        return f"Feedback - {self.comments[:30]}..."


class ContactMessage(models.Model):
    name = models.CharField(max_length=100, help_text='Name of the user.')
    email = models.EmailField(help_text='Email of the user.')
    submitted_at = models.DateTimeField(auto_now_add=True, help_text='Timestamp when each contact form was submitted.')

    def __str__(self):
        return self.name
