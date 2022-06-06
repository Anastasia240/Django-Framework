from django.contrib import admin
from django.utils.html import format_html

from mainapp.models import News, Course, Lesson, CoursesTeachers

admin.site.register(News)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CoursesTeachers)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'deleted')
    list_filter = ('deleted', 'created_at')
    ordering = ('pk',)
    list_per_page = 5
    search_fields = ('title', 'intro', 'body')

    def slug(self, obj):
        return format_html(
            '<a href="{}" target="_blank">{}</a>',
            obj.title.lower().replase(' ', '-'),
            obj.title
        )
    slug.short_description = 'Slug'

    def mark_as_delete(self,request,queryset):
        queryset.update(deleted=True)
    mark_as_delete.short_description = 'Пометить удалённым'
