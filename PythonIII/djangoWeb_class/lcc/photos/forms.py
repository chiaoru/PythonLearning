# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:22:35 2023

@author: USER
"""

from django import forms
from .models import Photo

class UploadModelForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image',)
        widgets = {
            'image':forms.FileInput(attrs={'class':'form-control-file'})
            }