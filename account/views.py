from datetime import date
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from account.models import Receipt, ReceiptRow
from account.serializers import ReceiptSerializer


def receipt(request, pk=None):
    if pk:
        obj = get_object_or_404(Receipt, id=id)
        scenario = 'Update'
    else:
        obj = Receipt(date=date.today())
        scenario = 'New'
    data = ReceiptSerializer(obj).data
    return render(request, 'receipt.html', {'scenario': scenario, 'data': data})