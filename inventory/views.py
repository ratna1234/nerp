import json
from datetime import date
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from models import Item, Category
from forms import ItemForm, CategoryForm, DemandForm
from inventory.filters import InventoryItemFilter
from inventory.models import Demand, DemandRow, delete_rows
from app.lib import invalid, save_model
from inventory.serializers import DemandSerializer, ItemSerializer


@login_required
def item_form(request, id=None):
    if id:
        item = get_object_or_404(Item, id=id)
        scenario = 'Update'
    else:
        item = Item()
        scenario = 'Create'
    if request.POST:
        form = ItemForm(data=request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('/inventory/items/')
    else:
        form = ItemForm(instance=item)
    if request.is_ajax():
        base_template = 'modal.html'
    else:
        base_template = 'base.html'
    return render(request, 'item_form.html', {
        'scenario': scenario,
        'form': form,
        'base_template': base_template,
    })


@login_required
def delete_inventory_item(request, id):
    object = get_object_or_404(Item, id=id)
    object.delete()
    return redirect('/inventory/items/')


@login_required
def list_inventory_items(request):
    objects = Item.objects.filter()
    filtered_items = InventoryItemFilter(request.GET, queryset=objects)
    return render(request, 'list_inventory_items.html', {'objects': filtered_items})


@login_required
def items_as_json(request):
    items = Item.objects.all()
    items_data = ItemSerializer(items).data
    return HttpResponse(json.dumps(items_data), mimetype="application/json")


@login_required
def list_categories(request):
    categories = Category.objects.filter()
    return render(request, 'list_inventory_categories.html', {'categories': categories})


@login_required
def create_category(request):
    category = Category()
    if request.POST:
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('/inventory/categories/')
    else:
        form = CategoryForm(instance=category)
    if request.is_ajax():
        base_template = 'modal.html'
    else:
        base_template = 'base.html'
    return render(request, 'inventory_category_create_form.html', {
        'form': form,
        'base_template': base_template,
    })


@login_required
def update_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.POST:
        form = CategoryForm(data=request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('/inventory/categories/')
    else:
        form = CategoryForm(instance=category)
    if request.is_ajax():
        base_template = 'modal.html'
    else:
        base_template = 'base.html'
    return render(request, 'inventory_category_update_form.html', {
        'form': form,
        'base_template': base_template
    })


@login_required
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('/inventory/categories/')


def demand_form(request, id=None):
    if id:
        object = get_object_or_404(Demand, id=id)
        scenario = 'Update'
    else:
        object = Demand(date=date.today())
        scenario = 'Create'
    if request.POST:
        form = DemandForm(request.POST, instance=object)
        if form.is_valid():
            object = form.save(commit=False)
            object.save()
        if id or form.is_valid():
            rows = json.loads(request.POST['rows'])
            model = DemandRow
            for index, row in enumerate(rows.get('rows')):
                if invalid(row, ['amount']):
                    continue
                values = {'sn': index + 1, 'cheque_number': row.get('cheque_number'),
                          'cheque_date': row.get('cheque_date'),
                          'drawee_bank': row.get('drawee_bank'), 'drawee_bank_address': row.get('drawee_bank_address'),
                          'amount': row.get('amount'), 'cheque_deposit': object}
                submodel, created = model.objects.get_or_create(id=row.get('id'), defaults=values)
                # set_transactions(submodel, request.POST.get('date'),
                #                  ['dr', bank_account, row.get('amount')],
                #                  ['cr', benefactor, row.get('amount')],
                # )
                if not created:
                    submodel = save_model(submodel, values)
            delete_rows(rows.get('deleted_rows'), model)
            return redirect('/bank/cheque-deposits/')
    form = DemandForm(instance=object)
    object_data = DemandSerializer(object).data
    return render(request, 'demand_form.html', {'form': form, 'data': object_data, 'scenario': scenario})