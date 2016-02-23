from django import forms
from practice.models import Message


class MessageForm(forms.Form):
    name = forms.CharField(
        max_length=100,
    )
    title = forms.CharField(
        max_length=100, required=False,
    )
    content = forms.CharField(
        widget=forms.Textarea,
    )

    def save(self):
        data = self.cleaned_data
        message = Message(
            name=data['name'],
            title=data['title'],
            content=data['content']
        )
        message.save()
        return message
