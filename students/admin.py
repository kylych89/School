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
        'photo_student',
        'klass'
    )
    readonly_fields = (
        'get_image',
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100"')
    
    get_image.short_description = "Image"