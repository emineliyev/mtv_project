from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import DraggableMPTTAdmin
from .models import Post, Category, Tag, Comment



class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
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
        return mark_safe(f'<img src="{obj.image.url}" width="50"')

    get_photo.short_description = 'Şəkil'


admin.site.register(
    Category,
    DraggableMPTTAdmin,
    prepopulated_fields={"slag": ("name",)},
    list_display=('tree_actions', 'indented_title', 'id'),
    list_display_links=('indented_title',),
    search_fields=('name',)
)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slag": ("name",)}
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)
