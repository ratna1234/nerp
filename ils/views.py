from django.shortcuts import render


# Create your views here.
def acquisition(request):
    return render(request, 'acquisition.html', {})