from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
import json
from django.http import HttpResponse, FileResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DetailView, CreateView
from datetime import datetime
from django.conf import settings

from mainapp.models import News, Course, Lesson


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
    permission_required = ('mainapp.add_news',)


class CourseDetailView(TemplateView):
    template_name = 'mainapp/courses_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['course_object'] = get_object_or_404(Course, pk=self.kwargs.get('pk'))
        context_data['lessons'] = Lesson.objects.filter(course=context_data['course_object'])
        context_data['teachers'] = CourseTeacher.objects.filter(course=context_data['course_object'])
        context_data['feelback_list'] = CourseFeedback.objects.filter(course=context_data['course_object'])
        if self.request.user.is_authenticated:
            context_data['feedback_form'] = CourseFeedback(
                course=context_data['course_object'],
                user=self.request.user

            )
        return context_data

    def get(self, *args, **kwargs):
        query = self.request.GET.get('q', None)
        return super.get(*args, **kwargs)


class CourseFeedbackCreateView(CreateView):
    model = CourseFeedback
    form_class = CourseFeedbackForm

    def form_valid(self, form):
        self.object = form.save()
        rendered_template = render_to_string('mainapp/includes/feedback_card.html', context={'item:'self.object})

class LogView(UserPassesTestMixin, TemplateView):
    template_name = 'mainapp/login.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        log_lines = []
        with open(settings.BASE_DIR / "log/main_log.log") as log_file:
            for i, line in enumerate(log_file):
                if i == 1000:
                    break
                log_lines.insert(0, line)

            context_data['logs'] = log_lines
        return context_data


class LogDownLoadView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, *args, **kwargs):
        return FileResponse(open(settings.LOG_FILE))
