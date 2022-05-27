from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.generic import TemplateView
from datetime import datetime
from django.conf import settings

from mainapp.models import News


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        #with open(settings.BASE_DIR / '001_news.json') as news_file:
        context_data['object_list'] = News.objects.all()
        return context_data

    def get(self, *args, **kwargs):
        query = self.request.GET.get('q', None)
        return super.get(*args, **kwargs)
