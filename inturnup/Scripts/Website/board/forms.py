from django import forms
from .models import UploadFileModel

class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.'
        },
        max_length=128, label="제목")
    contents = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'
        },
        widget=forms.Textarea, label="내용")
    file = forms.FileField(
        label='Select a file',
        help_text = 'max.42 megabytes'
    )

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()