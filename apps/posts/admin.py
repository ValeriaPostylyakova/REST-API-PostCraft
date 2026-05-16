from django.contrib import admin
from django.utils.html import format_html
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'get_tags', 'display_image', 'created_at')
    
    list_display_links = ('title',)
    
    list_filter = ('category', 'tags', 'created_at', 'user')
    
    search_fields = ('title', 'content', 'user__username', 'category__name', 'tags__name')
    
    readonly_fields = ('created_at', 'updated_at', 'preview_image')
    
    filter_horizontal = ('tags',)
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'content', 'user')
        }),
        ('Медиа и связи', {
            'fields': ('image_url', 'preview_image', 'category', 'tags')
        }),
        ('Даты системы', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',), # Скрывает блок по умолчанию
        }),
    )

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Теги'

    def display_image(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />', obj.image_url)
        return "Нет фото"
    display_image.short_description = 'Миниатюра'

    def preview_image(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" width="200" style="border-radius: 8px;" />', obj.image_url)
        return "Ссылка на изображение отсутствует"
    preview_image.short_description = 'Превью изображения'

