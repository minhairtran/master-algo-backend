from django import forms
from django.conf import settings

from .models import Feedback

MAX_FEEDBACK_LENGTH = settings.MAX_FEEDBACK_LENGTH

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if(len(content) > MAX_FEEDBACK_LENGTH):
            raise forms.ValidationError("This feedback is too long")
        return content