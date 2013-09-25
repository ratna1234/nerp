import json
from datetime import date

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

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


@login_required
def demand_form(request, id=None):
    print request.LANGUAGE_CODE
    if id:
        object = get_object_or_404(Demand, id=id)
        scenario = 'Update'
    else:
        object = Demand(date=date.today())
        scenario = 'Create'
    if request.POST:
        form = DemandForm(request.POST, instance=object)
        table = json.loads(request.POST['table_model'])
        if form.is_valid():
            object = form.save(commit=False)
            object.save()
        if id or form.is_valid():
            model = DemandRow
            for index, row in enumerate(table.get('rows')):
                print row
                if invalid(row, ['item_id', 'quantity', 'unit', 'release_quantity']):
                    continue
                values = {'sn': index + 1, 'item_id': row.get('item_id'),
                          'specification': row.get('specification'),
                          'quantity': row.get('quantity'), 'unit': row.get('unit'),
                          'release_quantity': row.get('release_quantity'), 'remarks': row.get('remarks'),
                          'demand': object}
                submodel, created = model.objects.get_or_create(id=row.get('id'), defaults=values)
                # set_transactions(submodel, request.POST.get('date'),
                #                  ['dr', bank_account, row.get('amount')],
                #                  ['cr', benefactor, row.get('amount')],
                # )
                if not created:
                    submodel = save_model(submodel, values)
            delete_rows(table.get('deleted_rows'), model)
            return redirect(reverse('list_inventory_items'))
    else:
        form = DemandForm(instance=object)
    object_data = DemandSerializer(object).data

    return render(request, 'demand_form.html',
                  {'form': form, 'data': object_data, 'scenario': scenario})


@login_required
def save_demand(request):
    params = json.loads(request.body)
    dct = {'rows': {}}
    object_values = {'release_no': params.get('release_no'), 'fiscal_year': params.get('fiscal_year'),
                     'date': params.get('date'), 'purpose': params.get('purpose'),
                     'demandee_id': params.get('demandee')}
    if params.get('id'):
        object = Demand.objects.get(id=params.get('id'))
    else:
        object = Demand()
    try:
        object = save_model(object, object_values)
    except Exception as e:
        import pdb
        pdb.set_trace()
        if hasattr(e, 'messages'):
            dct['error_message'] = '; '.join(e.messages)
        elif str(e) != '':
            dct['error_message'] = str(e)
    dct['id'] = object.id
    model = DemandRow
    for index, row in enumerate(params.get('table_view').get('rows')):
        print row
        if invalid(row, ['item_id', 'quantity', 'unit', 'release_quantity']):
            continue
        values = {'sn': index + 1, 'item_id': row.get('item_id'),
                  'specification': row.get('specification'),
                  'quantity': row.get('quantity'), 'unit': row.get('unit'),
                  'release_quantity': row.get('release_quantity'), 'remarks': row.get('remarks'),
                  'demand': object}
        submodel, created = model.objects.get_or_create(id=row.get('id'), defaults=values)
        # set_transactions(submodel, request.POST.get('date'),
        #                  ['dr', bank_account, row.get('amount')],
        #                  ['cr', benefactor, row.get('amount')],
        # )
        if not created:
            submodel = save_model(submodel, values)
        dct['rows'][index] = submodel.id
    delete_rows(params.get('table_view').get('deleted_rows'), model)
    return HttpResponse(json.dumps(dct), mimetype="application/json")


@login_required
def delete_demand(request, id):
    object = get_object_or_404(Demand, id=id)
    object.delete()
    return redirect(reverse('list_inventory_items'))