from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pymongo import MongoClient
from bson.objectid import ObjectId

from inventory.forms import CategoryForm


@login_required
def category_form(request, id=None):
    client = MongoClient()
    db = client.goms
    collection = db.inventory_category
    if id:
        scenario = 'Update'
        item = collection.find_one({'_id': ObjectId(id)})
    else:
        scenario = 'Create'
        item = None
    if request.POST:
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            collection.insert(form.cleaned_data)
            print form.cleaned_data
            pass
    else:
        form = CategoryForm(data=item)
    return render(request, 'category_form.html', {
        'form': form,
        'scenario': scenario,
    })



