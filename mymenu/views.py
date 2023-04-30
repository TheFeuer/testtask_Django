from django.shortcuts import render


def base(request, slug=None):
    return render(request, 'base.html')