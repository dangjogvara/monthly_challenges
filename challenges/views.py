from django.http import HttpResponse
from django.shortcuts import render


def monthly_challenge(request, month):
    return HttpResponse(month)
