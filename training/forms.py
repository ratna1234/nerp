from django import forms

from app.libr import KOModelForm, UserModelChoiceField
from models import Training, Category, TargetGroup, ResourcePerson
from users.models import User
from django.utils.translation import ugettext_lazy as _


class TrainingForm(KOModelForm):
    #category = TreeNodeChoiceField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Training


class CategoryForm(KOModelForm):
    class Meta:
        model = Category


class ResourcePersonForm(KOModelForm):
    class Meta:
        model = ResourcePerson


class TargetGroupForm(KOModelForm):
    class Meta:
        model = TargetGroup