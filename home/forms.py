from django import forms
from .models import Feedback, ContactMessage


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comments']
        widgets = {
            'comments': forms.Textarea(attrs={'placeholder':'Enter your feedback...', 'rows':4})
        }


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email']