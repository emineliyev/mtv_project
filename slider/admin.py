from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import Slider

class SliderAdminForm(forms.ModelForm):

    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Slider
        fields = '__all__'


class SliderAdmin(admin.ModelAdmin):
    form = SliderAdminForm
    list_display = (
        'id',
        'title',
        'author',
        'get_photo',
        'category',
        'view',
        'create_at',
        'published',
    )
    list_filter = ('published', )
    search_fields = ('title', )
    list_editable = ('published', )
    save_on_top = True
    list_display_links = ('id', 'title')
    fields = (
        'title',
        'description',
        'author',
        'image',
        'category',
        'tag',
        'view',
        'create_at',
        'published',
    )
    readonly_fields = (
        'get_photo',
        'view',
        'create_at',
    )

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100"')

    get_photo.short_description = 'Şəkil'


admin.site.register(Slider, SliderAdmin)
