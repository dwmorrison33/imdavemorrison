from django.shortcuts import render


def my_site(request):
    return render(request, 'mysite/my-site.html')
