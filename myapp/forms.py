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
    # def clean_latitude(self):
    #     data=self.cleaned_data['latitude']
    #     if float(data)>=-90 and float(data)<=90:
    #         print("valid")
    #     else:
    #         raise ValidationError(('Wrong coordinates entered'))
    #     return data
    # def clean_longitude(self):
    #     data=self.cleaned_data['longitude']
    #     if float(data)>=-90 and float(data)<=90:
    #         print("valid")
    #     else:
    #         raise ValidationError(('Wrong coordinates entered'))
    class Meta:
        model=Node
        fields= ('installedDate','isMQ135','isMQ5','isMQ7','latitude','longitude')