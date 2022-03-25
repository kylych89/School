from django.contrib import admin
from django.utils.safestring import mark_safe

from School.director.models import Director

# Register your models here.

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'image',
        'phone',
    )
    readonly_fields = (
        'get_image',
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100"')
    
    get_image.short_description = "Image"