from django.shortcuts import render
from django.views import View

links = [{"title": "Мои приключения", "link": "adventures"}, {"title": "Мои фотографии", "link": "photos"},
         {"title": "Реклама у меня", "link": "promo"}, {"title": "Контакты", "link": "contacts"}, ]

categories = [
    {"id": "drinks", "title": "Напитки"},
    {"id": "streetfood", "title": "Стритфуд"},
    {"id": "lunches", "title": "Обеды"}
]


class VacancyView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "vacancy/vacancy.html", {"links": links, "categories": categories})
