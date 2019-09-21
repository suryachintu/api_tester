from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render


# Create your views here.
from stats.models import TestCase


def index(request):
    context = {}
    return render(request, 'stats/main.html', context)


def add_test_case(request):
    if request.method == 'POST':
        testcase = TestCase()
        testcase.endpoint_url = request.POST['api_url']
        testcase.headers = request.POST['headers']
        testcase.params = request.POST['query_params']
        testcase.expected_response_code = request.POST['response_code']
        testcase.save()
        return HttpResponse('Success')
    else:
        return HttpResponseForbidden('403 Forbidden')
