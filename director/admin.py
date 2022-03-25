from django.contrib import admin
from django.utils.safestring import mark_safe

from director.models import Director

# Register your models here.

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'image',
        'phone',
    )
    read_only = (
        'get_image',
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" heigth="100">')
    
    get_image.short_description = "Image"