from django import forms
from .models import Project


class ContactFrom(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['income', 'costum']


class Expense_addFrom(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['salary', 'markiting']

class AddProjectFrom(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']
