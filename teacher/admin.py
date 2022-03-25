from django.contrib import admin
from django.utils.safestring import mark_safe
from teacher.models import Teacher

# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'teacher_name',
        'teacher_last_name',
        'phone',
        'address',
        'get_image'
    )
    readonly_fields = (
        'get_image',
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100"')
    
    get_image.short_description = "Image"