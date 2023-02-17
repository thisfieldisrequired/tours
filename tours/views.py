from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "tours/index.html", {})


class AboutPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "tours/about.html", {})


class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tours/test.html', {'name': 'Alex', 'place': 'Here'})


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
