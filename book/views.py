from django.http import HttpResponse

def my_book(request):
    return HttpResponse("Welcome to the book app!")
