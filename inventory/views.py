import json
from datetime import date

from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from livesettings import config_value

from inventory.forms import ItemForm, CategoryForm, DemandForm, PartyForm, PurchaseOrderForm
from inventory.filters import InventoryItemFilter
from inventory.models import Demand, DemandRow, delete_rows, Item, Category, Party, PurchaseOrder, PurchaseOrderRow
from app.lib import invalid, save_model
from inventory.serializers import DemandSerializer, ItemSerializer, PartySerializer, PurchaseOrderSerializer
from app.nepdate import BSUtil


@login_required
def item_form(request, id=None):
    if id:
        item = get_object_or_404(Item, id=id)
        scenario = _('Update')
    else:
        item = Item()
        scenario = _('Create')
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
    objects = Item.objects.all()
    filtered_items = InventoryItemFilter(request.GET, queryset=objects)
    return render(request, 'list_inventory_items.html', {'objects': filtered_items})


@login_required
def list_demand_forms(request):
    objects = Demand.objects.all()
    return render(request, 'list_demand_forms.html', {'objects': objects})


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
        scenario = _('Update')
    else:
        object = Demand(date=BSUtil().today())
        scenario = _('Create')
    form = DemandForm(instance=object)
    object_data = DemandSerializer(object).data
    return render(request, 'demand_form.html',
                  {'form': form, 'data': object_data, 'scenario': scenario})


@login_required
def save_demand(request):
    params = json.loads(request.body)
    dct = {'rows': {}}
    object_values = {'release_no': params.get('release_no'), 'fiscal_year': config_value('app', 'fiscal_year'),
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
        else:
            dct['error_message'] = 'Error in form data!'
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


@login_required
def list_parties(request):
    objects = Party.objects.all()
    return render(request, 'list_parties.html', {'objects': objects})


@login_required
def party_form(request, id=None):
    if id:
        object = get_object_or_404(Party, id=id)
        scenario = _('Update')
    else:
        object = Party()
        scenario = _('Create')
    if request.POST:
        form = PartyForm(data=request.POST, instance=object)
        if form.is_valid():
            object = form.save(commit=False)
            object.save()
            return redirect(reverse('list_parties'))
    else:
        form = PartyForm(instance=object)
    if request.is_ajax():
        base_template = 'modal.html'
    else:
        base_template = 'base.html'
    return render(request, 'party_form.html', {
        'scenario': scenario,
        'form': form,
        'base_template': base_template,
    })


@login_required
def delete_party(request, id):
    object = get_object_or_404(Party, id=id)
    object.delete()
    return redirect(reverse('list_inventory_items'))


@login_required
def parties_as_json(request):
    objects = Party.objects.all()
    objects_data = PartySerializer(objects).data
    return HttpResponse(json.dumps(objects_data), mimetype="application/json")


@login_required
def purchase_order(request, id=None):
    if id:
        object = get_object_or_404(PurchaseOrder, id=id)
        scenario = _('Update')
    else:
        object = PurchaseOrder(date=date.today())
        scenario = _('Create')
    form = PurchaseOrderForm(instance=object)
    object_data = PurchaseOrderSerializer(object).data
    return render(request, 'purchase_order.html',
                  {'form': form, 'data': object_data, 'scenario': scenario})


@login_required
def save_purchase_order(request):
    params = json.loads(request.body)
    dct = {'rows': {}}
    object_values = {'release_no': params.get('release_no'), 'fiscal_year': params.get('fiscal_year'),
                     'date': params.get('date'), 'purpose': params.get('purpose'),
                     'demandee_id': params.get('demandee')}
    if params.get('id'):
        object = PurchaseOrder.objects.get(id=params.get('id'))
    else:
        object = PurchaseOrder()
    try:
        object = save_model(object, object_values)
    except Exception as e:
        if hasattr(e, 'messages'):
            dct['error_message'] = '; '.join(e.messages)
        elif str(e) != '':
            dct['error_message'] = str(e)
        else:
            dct['error_message'] = 'Error in form data!'
    dct['id'] = object.id
    model = PurchaseOrderRow
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
