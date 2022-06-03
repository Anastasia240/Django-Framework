from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
import json
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView
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
    model = News
    paginate_by = 5
    template_name = 'mainapp/news.html'

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class NewsDetailView(DetailView):
    model = News


class NewsCreateView(PermissionRequiredMixin, CreateView):
    model = News
    fields = '__all__'
    success_url = reverse_lazy('main:news')
    permission_required = ('mainapp.add_news')

    def get(self, *args, **kwargs):
        query = self.request.GET.get('q', None)
        return super.get(*args, **kwargs)


