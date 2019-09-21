from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render


# Create your views here.

def index(request):
    context = {}
    return render(request, 'stats/main.html', context)


def add_test_case(request):
    if request.method == 'POST':
        return HttpResponse('Success')
    else:
        return HttpResponseForbidden('403 Forbidden')
