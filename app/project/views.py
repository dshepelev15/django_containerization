from django.http.response import HttpResponse


def index(request):
    return HttpResponse('Hello, world from gunicorn worker!')
