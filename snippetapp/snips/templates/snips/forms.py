from django import forms

from .models import Snips

class AddSnips(forms.ModelForm):

    class Meta:
        model = Snips
        fields = ('title','language', 'description', 'snip')


class SnipsCreate(forms.ModelForm):

    class Meta:
        model = Snippets
        fields = ('title','language', 'description', 'snip')
