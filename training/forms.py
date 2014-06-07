from django import forms

from app.libr import KOModelForm, UserModelChoiceField
from models import Training, Category, TargetGroup, ResourcePerson
from users.models import User
from django.utils.translation import ugettext_lazy as _


class TrainingForm(forms.ModelForm):
    #category = TreeNodeChoiceField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Training


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category


class ResourcePersonForm(forms.ModelForm):
    class Meta:
        model = ResourcePerson


class TargetGroupForm(forms.ModelForm):
    class Meta:
        model = TargetGroup