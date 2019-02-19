from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def mycity(request):
    return HttpResponse("Memphis All Day!!")
def myeats(request):
    return HttpResponse("Benihana")