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


# Restaurant's location model.
class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255, help_text='Address of the restaurant location.')
    city = models.CharField(max_length=100, help_text='City of the restaurant location.')
    state = models.CharField(max_length=100, help_text='State of the restaurant location.')
    zip_code = models.CharField(max_length=20, help_text='Zip code of the restaurant location.')

    # String representation of the RestaurantLocation model
    def __str__(self):
        return self.address

