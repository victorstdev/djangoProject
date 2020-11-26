from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
  message = forms.CharField(
    widget=forms.Textarea(attrs={'rows':5, 'placeholder':'What\'s on your mind?'}),
    max_length=4000,
    help_text='Max length of text is 4000')

  class Meta:
    model = Topic
    fields = ['subject', 'message']