from django import forms
from .models import Node, Pollution_Data
from django.core.exceptions import ValidationError
import re


class NewNodeForm(forms.ModelForm):
    class Meta:
        model=Node
        fields= ('installedDate','isMQ135','isMQ5','isMQ7','latitude','longitude')