from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render


def main_view(request):
    return render(request, 'tours/index.html')


def departure_view(request, departure):
    return render(request, 'tours/departure.html')


def tour_view(request, tour_id):
    return render(request, 'tours/tour.html')


def custom_handler404(request, exception):
    return HttpResponseNotFound("Page not found")


def custom_handler500(request):
    return HttpResponseServerError("Server error")
