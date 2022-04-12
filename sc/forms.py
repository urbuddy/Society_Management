from django import forms
from .models import Notice, Complaint


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of the Notice'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description of the Notice'}),
        }


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Complaint or Suggestion'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description of the Complaint or Suggestion'}),
        }