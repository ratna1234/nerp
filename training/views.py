from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from training.forms import TrainingForm, CategoryForm, TargetGroupForm, ResourcePersonForm, ParticipantForm, OrganizationForm
from training.models import Training, Category, ResourcePerson, TargetGroup, Participant, Organization, File
import json
from training.serializers import ParticipantSerializer, OrganizationSerializer, FileSerializer


def index(request):
    pass


def participants_as_json(request):
    items = Participant.objects.all()
    items_data = ParticipantSerializer(items).data
    return HttpResponse(json.dumps(items_data), mimetype="application/json")


def print_training(request, pk):
    item = get_object_or_404(Training, pk=pk)
    return render(request, 'print_training.html', {'obj': item})


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
            item = form.save(commit=False)
            if item.starts == '':
                item.starts = None
            if item.ends == '':
                item.ends = None
            item.save()
            form.save_m2m()
            item.participants.clear()
            participants = request.POST.get('selected_participants').split(',')
            for participant in participants:
                if participant == u'':
                    continue
                participant_obj = Participant.objects.get(pk=participant)
                item.participants.add(participant_obj)
                # return redirect('/inventory/items/')
        descriptions = request.POST.getlist('descriptions')
        file_ids = request.POST.getlist('file_ids')
        if request.POST.get('deleted_files') == '':
            deleted_files = []
        else:
            deleted_files = request.POST.get('deleted_files').split(',')

        for index in request.POST.getlist('indices'):
            ind = int(index)
            file_id = file_ids[ind]
            if file_id == u'':
                the_file = File()
            else:
                the_file = File.objects.get(id=file_id)
            the_file.description = descriptions[ind]
            if request.FILES.get('files[' + index + ']'):
                the_file.file = request.FILES.get('files[' + index + ']')
            elif request.POST.get('clears[' + index + ']'):
                the_file.file = None
            the_file.training = item
            the_file.save()
        for deleted_file_id in deleted_files:
            # if deleted_file_id == '':
            #     continue
            # try:
            the_file = File.objects.get(id=deleted_file_id)
            the_file.delete()
            # except File.DoesNotExist:
            #     pass


    else:
        form = TrainingForm(instance=item)
    if scenario == 'Update':
        participants = [x.id for x in item.participants.all()]
        training_files = item.files.all()
    else:
        participants = []
        training_files = []
    files = FileSerializer(training_files).data
    return render(request, 'training_form.html', {
        'scenario': scenario,
        'form': form,
        'base_template': 'training_base.html',
        'category_form': CategoryForm(instance=Category()),
        'resource_person_form': ResourcePersonForm(instance=ResourcePerson()),
        'target_group_form': TargetGroupForm(instance=TargetGroup()),
        'participant_form': ParticipantForm(instance=Participant()),
        'organization_form': OrganizationForm(instance=Organization()),
        'participants': participants,
        'files': files,
        'training_files': training_files,
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
            return redirect(reverse('list_categories'))
    else:
        form = CategoryForm(instance=item)
    return render(request, 'category_form.html', {
        'scenario': scenario,
        'form': form,
        'base_template': 'training_base.html',
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
            return redirect(reverse('list_resource_persons'))
    else:
        form = ResourcePersonForm(instance=item)
    return render(request, 'resource_person_form.html', {
        'scenario': scenario,
        'form': form,
        'base_template': 'training_base.html',
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
            return redirect(reverse('list_target_groups'))
    else:
        form = TargetGroupForm(instance=item)
    return render(request, 'target_group_form.html', {
        'scenario': scenario,
        'form': form,
        'base_template': 'training_base.html',
    })


def participant_form(request, pk=None):
    if pk:
        item = get_object_or_404(Participant, pk=pk)
        scenario = 'Update'
    else:
        item = Participant()
        scenario = 'Create'
    if request.POST:
        form = ParticipantForm(data=request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            if request.is_ajax():
                return HttpResponse(json.dumps(ParticipantSerializer(item).data), mimetype="application/json")
            return redirect(reverse('list_participants'))
    else:
        form = ParticipantForm(instance=item)
    return render(request, 'participant_form.html', {
        'scenario': scenario,
        'form': form,
        'base_template': 'training_base.html',
    })


def organization_form(request, pk=None):
    if pk:
        item = get_object_or_404(Organization, pk=pk)
        scenario = 'Update'
    else:
        item = Organization()
        scenario = 'Create'
    if request.POST:
        form = OrganizationForm(data=request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            if request.is_ajax():
                # return HttpResponse(json.dumps(OrganizationSerializer(item).data), mimetype="application/json")
                return render(request, 'callback.html', {'obj': OrganizationSerializer(item).data})
            return redirect(reverse('list_organizations'))
    else:
        form = OrganizationForm(instance=item)
    if request.is_ajax():
        base_template = 'modal.html'
    else:
        base_template = 'training_base.html'
    return render(request, 'organization_form.html', {
        'scenario': scenario,
        'form': form,
        'base_template': base_template,
    })


def list_trainings(request):
    items = Training.objects.all()
    return render(request, 'list_trainings.html', {'objects': items})


def list_participants(request):
    items = Participant.objects.all()
    return render(request, 'list_participants.html', {'objects': items})


def list_organizations(request):
    items = Organization.objects.all()
    return render(request, 'list_organizations.html', {'objects': items})


def list_resource_persons(request):
    items = ResourcePerson.objects.all()
    return render(request, 'list_resource_persons.html', {'objects': items})


def list_target_groups(request):
    items = TargetGroup.objects.all()
    return render(request, 'list_target_groups.html', {'objects': items})


def list_categories(request):
    items = Category.objects.all()
    return render(request, 'list_categories.html', {'objects': items})


def list_files(request):
    items = File.objects.all()
    return render(request, 'list_files.html', {'objects': items})


def delete_training(request, pk):
    obj = get_object_or_404(Training, pk=pk)
    obj.delete()
    return redirect(reverse('list_trainings'))


def delete_participant(request, pk):
    obj = get_object_or_404(Participant, pk=pk)
    obj.delete()
    return redirect(reverse('list_participants'))


def delete_organization(request, pk):
    obj = get_object_or_404(Organization, pk=pk)
    obj.delete()
    return redirect(reverse('list_organizations'))


def delete_category(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    obj.delete()
    return redirect(reverse('list_categories'))


def delete_target_group(request, pk):
    obj = get_object_or_404(TargetGroup, pk=pk)
    obj.delete()
    return redirect(reverse('list_target_groups'))


def delete_resource_person(request, pk):
    obj = get_object_or_404(ResourcePerson, pk=pk)
    obj.delete()
    return redirect(reverse('list_resource_persons'))