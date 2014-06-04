from django import forms

from app.libr import KOModelForm, UserModelChoiceField
from models import Training
from users.models import User
from django.utils.translation import ugettext_lazy as _


class TrainingForm(KOModelForm):
    #category = TreeNodeChoiceField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Training

