# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse

import os
import re

from django import forms
from django.forms import ModelChoiceField
from django.shortcuts import render, get_object_or_404, redirect


class ExtFileField(forms.FileField):
    """
    Same as forms.FileField, but you can specify a file extension whitelist.

    Traceback (most recent call last):
    ...
    ValidationError: [u'Not allowed filetype!']
    """

    def __init__(self, *args, **kwargs):
        ext_whitelist = kwargs.pop("ext_whitelist")
        self.ext_whitelist = [i.lower() for i in ext_whitelist]

        super(ExtFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(ExtFileField, self).clean(*args, **kwargs)
        if data is None:
            if self.required:
                raise forms.ValidationError("This file is required")
            else:
                return
        elif data is not False:
            filename = data.name
            ext = os.path.splitext(filename)[1]
            ext = ext.lower()
            if ext not in self.ext_whitelist:
                file_types = ", ".join([i for i in self.ext_whitelist])
                error = "Only allowed file types are: %s" % file_types
                raise forms.ValidationError(error)


class KOModelForm(forms.ModelForm):
    class EmailTypeInput(forms.widgets.TextInput):
        input_type = 'email'

    class NumberTypeInput(forms.widgets.TextInput):
        input_type = 'number'

    class TelephoneTypeInput(forms.widgets.TextInput):
        input_type = 'tel'

    class DateTypeInput(forms.widgets.DateInput):
        input_type = 'date'

    class DateTimeTypeInput(forms.widgets.DateTimeInput):
        input_type = 'datetime'

    class TimeTypeInput(forms.widgets.TimeInput):
        input_type = 'time'

    def __init__(self, *args, **kwargs):
        super(KOModelForm, self).__init__(*args, **kwargs)
        self.refine()

    def refine(self):
        for (name, field) in self.fields.items():
            # add HTML5 required attribute for required fields
            if field.required:
                field.widget.attrs['required'] = 'required'
            field.widget.attrs['data-bind'] = 'value: ' + name


def invalid(row, required_fields):
    invalid_attrs = []
    for attr in required_fields:
        # if one of the required attributes isn't received or is an empty string
        if not attr in row or row.get(attr) == "":
            invalid_attrs.append(attr)
    if len(invalid_attrs) is 0:
        return False
    return invalid_attrs


def all_empty(row, required_fields):
    empty = True
    for attr in required_fields:
        # if one of the required attributes isn received or is not an empty string
        if attr in row and row.get(attr) != "":
            empty = False
    return empty


def save_model(model, values):
    for key, value in values.items():
        setattr(model, key, value)
    model.save()
    return model


def zero_for_none(obj):
    if obj is None:
        return 0
    else:
        return obj


def none_for_zero(obj):
    if not obj:
        return None
    else:
        return obj


def add(*args):
    total = 0
    for arg in args:
        if arg == '':
            arg = 0
        total += float(arg)
    return total


def digitize(n):
    if n is None:
        return None
    d = {
        '०': '0',
        '१': '1',
        '२': '2',
        '३': '3',
        '४': '4',
        '५': '5',
        '६': '6',
        '७': '7',
        '८': '8',
        '९': '9'
    }
    pattern = re.compile('|'.join(d.keys()))
    result = pattern.sub(lambda x: d[x.group()], unicode(n))
    return float(result)
    # devanagari_nums = ('०','१','२','३','४','५','६','७','८','९')
    # return ''.join(devanagari_nums[int(digit)] for digit in str(n))


class UserModelChoiceField(ModelChoiceField):
    '''
    A ModelChoiceField to represent User
    select boxes in the Auto Admin
    '''

    def label_from_instance(self, obj):
        return "%s" % (obj.full_name)


def form_view(some_func):
    def inner(*args, **kwargs):
        dct = some_func(args, kwargs)
        request = (args)[0]
        id = kwargs.get('id')
        if id:
            obj = get_object_or_404(dct['model'], id=id)
            scenario = 'Update'
        else:
            obj = dct['model']()
            scenario = 'Create'
        if request.POST:
            form = dct['form'](data=request.POST, instance=obj)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                if request.is_ajax():
                    return render(request, 'callback.html', {'obj': dct['serializer'](obj).data})
                return redirect(reverse(dct['listing_url']))
        else:
            form = dct['form'](instance=obj)
        if request.is_ajax():
            base_template = 'modal.html'
        else:
            base_template = 'base.html'
        return render(request, dct['template'], {
            'scenario': scenario,
            'form': form,
            'base_template': base_template,
        })

    return inner