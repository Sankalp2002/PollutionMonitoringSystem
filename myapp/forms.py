from django import forms
from .models import Node, Pollution_Data
from django.core.exceptions import ValidationError
import re
from datetime import date


class NewNodeForm(forms.ModelForm):
    def clean_installedDate(self):
        data=self.cleaned_data['installedDate']
        if isinstance(data,type(date.today())) and data<=date.today():
            print("valid")
        else:
            raise ValidationError(('Wrong date entered'))
        return data
    class Meta:
        model=Node
        fields= ('installedDate','location')