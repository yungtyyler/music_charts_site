from django import forms
from .models import Post, Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full py-4 rounded-xl border px-4'
            })
        }

class TopicPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 rounded-xl border px-4'
            })
        }