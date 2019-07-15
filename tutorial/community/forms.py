from django.forms import ModelForm
from community.models import *

class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'title', 'contents', 'url', 'email']
        """
        아까 생성한 article로 쉽게 form 생성 가능
        표시할 field 나열. 생성해놓은 애들 나열
        """
