from django import forms
from .models import Usergroup

class GroupForm(forms.ModelForm):
    class Meta:
        model = Usergroup
        fields = ('groupname','group_img','group_info')