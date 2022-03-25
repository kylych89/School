from django.contrib import admin
from django.utils.safestring import mark_safe

from students.models import Students

# Register your models here.
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'number_parents',
        'place_of_residence',
        'klass',
        'get_image'
    )
    readonly_fields = (
        'get_image',
    )

    def get_image(self, obj):
        return mark_safe(f'<img src= {obj.photo_student.url} width="100" heigth="110">')

    get_image.short_description = "Image"