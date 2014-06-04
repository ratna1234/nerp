from django.shortcuts import render, get_object_or_404
from training.forms import TrainingForm
from training.models import Training


def index(request):
    pass


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
    return render(request, 'training_form.html', {
        'scenario': scenario,
        'form': form,
        'base_template': 'base.html',
    })


