from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from training.forms import TrainingForm, CategoryForm, TargetGroupForm, ResourcePersonForm
from training.models import Training, Category, ResourcePerson, TargetGroup, Participant
import json
from training.serializers import ParticipantSerializer


def index(request):
    pass


def participants_as_json(request):
    items = Participant.objects.all()
    items_data = ParticipantSerializer(items).data
    return HttpResponse(json.dumps(items_data), mimetype="application/json")


def training_form(request, pk=None):
    if pk:
        item = get_object_or_404(Training, pk=pk)
        scenario = 'Update'
    else:
        item = Training()
        scenario = 'Add'

    if request.POST:
        form = TrainingForm(data=request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            # if request.is_ajax():
            #     return render(request, 'callback.html', {'obj': ItemSerializer(item).data})
            # return redirect('/inventory/items/')
    else:
        form = TrainingForm(instance=item)
    category_form = CategoryForm(instance=Category())
    resource_person_form = ResourcePersonForm(instance=ResourcePerson())
    target_group_form = TargetGroupForm(instance=TargetGroup())
    return render(request, 'training_form.html', {
        'scenario': scenario,
        'form': form,
        'base_template': 'base.html',
        'category_form': category_form,
        'resource_person_form': resource_person_form,
        'target_group_form': target_group_form,
        'participants': [x.id for x in item.participants.all()]
    })


def category_form(request, pk=None):
    if pk:
        item = get_object_or_404(Category, pk=pk)
        scenario = 'Update'
    else:
        item = Category()
        scenario = 'Create'
    if request.POST:
        form = CategoryForm(data=request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            if request.is_ajax():
                return HttpResponse(json.dumps({'id': item.id, 'name': item.name}), mimetype="application/json")
            return redirect('/inventory/items/')
    else:
        form = CategoryForm(instance=item)
    return render(request, 'category_form.html', {
        'scenario': scenario,
        'form': form,
        'base_template': 'base.html',
    })


def resource_person_form(request, pk=None):
    if pk:
        item = get_object_or_404(ResourcePerson, pk=pk)
        scenario = 'Update'
    else:
        item = ResourcePerson()
        scenario = 'Create'
    if request.POST:
        form = ResourcePersonForm(data=request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            if request.is_ajax():
                return HttpResponse(json.dumps({'id': item.id, 'name': item.name}), mimetype="application/json")
            return redirect('/inventory/items/')
    else:
        form = ResourcePersonForm(instance=item)
    return render(request, 'resource_person_form.html', {
        'scenario': scenario,
        'form': form,
        'base_template': 'base.html',
    })


def target_group_form(request, pk=None):
    if pk:
        item = get_object_or_404(TargetGroup, pk=pk)
        scenario = 'Update'
    else:
        item = TargetGroup()
        scenario = 'Create'
    if request.POST:
        form = TargetGroupForm(data=request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            if request.is_ajax():
                return HttpResponse(json.dumps({'id': item.id, 'name': item.name}), mimetype="application/json")
            return redirect('/inventory/items/')
    else:
        form = TargetGroupForm(instance=item)
    return render(request, 'target_group_form.html', {
        'scenario': scenario,
        'form': form,
        'base_template': 'base.html',
    })