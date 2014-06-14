from django import forms
from django.core.urlresolvers import reverse_lazy
from models import Training, Category, TargetGroup, ResourcePerson, Participant, Organization


class TrainingForm(forms.ModelForm):
    #category = TreeNodeChoiceField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Training


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category


class ResourcePersonForm(forms.ModelForm):
    organization = forms.ModelChoiceField(Organization.objects.all(), widget=forms.Select(
        attrs={'class': 'selectize', 'data-url': reverse_lazy('add_organization')}))

    class Meta:
        model = ResourcePerson


class TargetGroupForm(forms.ModelForm):
    class Meta:
        model = TargetGroup


class ParticipantForm(forms.ModelForm):
    organization = forms.ModelChoiceField(Organization.objects.all(), widget=forms.Select(
        attrs={'class': 'selectize', 'data-url': reverse_lazy('add_organization')}))

    class Meta:
        model = Participant


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization