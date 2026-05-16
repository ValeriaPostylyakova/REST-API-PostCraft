from django.contrib import admin
from .models import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'slug', 'created_at', 'updated_at')
	list_display_links = ('id', 'name')
	search_fields = ('name', 'slug')
	list_filter = ('created_at', 'updated_at')
	readonly_fields = ('created_at', 'updated_at')
	prepopulated_fields = {'slug': ('name',)}
	ordering = ('-created_at',)
	list_per_page = 20
