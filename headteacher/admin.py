from django.contrib import admin
from django.utils.safestring import mark_safe

from headteacher.models import HeadTeacher



@admin.register(HeadTeacher)
class HeadTeacherAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'get_image',
    )

    read_only = (
        'get_image',
    )

    def get_image(self, obj):
        return mark_safe(f'<img src= {obj.image_head_teacher.url} width="100" heigth="110">')

    get_image.short_description = "Image"
