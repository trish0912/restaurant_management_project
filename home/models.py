from django.db import models

# Create your models here.
class Feedback(models.Model):
    comments = models.TextField()

    def __str__(self):
        return f"Feedback - {self.comments[:30]}..."


class ContactMessage(models.Model):
    name = models.CharField(max_length=100, help_text='Name of the user.')
    email = models.EmailField(help_text='Email of the user.')
    message = models.TextField(help_text='Contact Message')
    submitted_at = models.DateTimeField(auto_now_add=True, help_text='Timestamp when each contact form was submitted.')

    def __str__(self):
        return f"{self.name}-{self.email}"


# Restaurant's location model.
class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255, help_text='Address of the restaurant location.')
    city = models.CharField(max_length=100, help_text='City of the restaurant location.')
    state = models.CharField(max_length=100, help_text='State of the restaurant location.')
    zip_code = models.CharField(max_length=20, help_text='Zip code of the restaurant location.')
    phone_number = models.CharField(max_length=15, blank=True, null=True, help_text='Phone number of the restaurant.')

    # Storing opening hours as JSON
    opening_hours = models.JSONField(default=dict)

    # String representation of the RestaurantLocation model
    def __str__(self):
        return self.address

