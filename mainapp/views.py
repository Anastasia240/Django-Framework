from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from datetime import datetime


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


def get_context_data(self, **kwargs):
    context_data = super().get_context_data(**kwargs)
    context_data['object_list'] = [
        {
            'title': 'Новость раз',
            'preview': 'Превью к новости раз',
            'date': '2022-05-01'
        },

        {
            'title': 'Новость два',
            'preview': 'Превью к новости два',
            'date': '2022-05-02'
        },
        {
            'title': 'Новость три',
            'preview': 'Превью к новости три',
            'date': '2022-05-03'
        },
        {
            'title': 'Новость четыре ',
            'preview': 'Превью к новости четыре',
            'date': '2022-05-04'
        },
        {
            'title': 'Новость пять',
            'preview': 'Превью к новости пять',
            'date': '2022-05-05'
        },

        {
            'title': 'Новость шесть',
            'preview': 'Превью к новости шесть',
            'date': '2022-05-06'
        },

    ]
    return context_data


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'
