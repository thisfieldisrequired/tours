from django.shortcuts import render
from django.views import View


class VacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "vacancy/vacancy.html", {})
