from django.shortcuts import render
from django.http import HttpResponse


def main1(request):
    '''
    Show 'Hello world!' in the main1 page
    '''
    return HttpResponse('歡迎光臨本書店，來杯提神的咖啡，看本好書吧！')
# Create your views here.
