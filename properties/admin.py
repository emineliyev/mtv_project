from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Contacts, Logo, Advertising


class LogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_photo')

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50"')


class AdvertisingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'customer_url',
        'get_photo',
        'published',
        'create_at',
    )
    list_display_links = ('id', 'customer')
    list_filter = ('published', )
    search_fields = ('customer', )
    list_editable = ('published',)

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50"')


admin.site.register(Contacts)
admin.site.register(Logo, LogoAdmin)
admin.site.register(Advertising, AdvertisingAdmin)