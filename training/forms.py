from django import forms
from models import Training, Category, TargetGroup, ResourcePerson, Participant


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


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant