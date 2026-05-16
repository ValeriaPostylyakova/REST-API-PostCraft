from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Профиль пользователя'
    readonly_fields = ('preview_avatar',)
    fields = ('first_name', 'last_name', 'bio', 'avatar', 'preview_avatar')

    def preview_avatar(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="150" style="border-radius: 8px;" />', obj.avatar)
        return "Аватар отсутствует"
    preview_avatar.short_description = 'Превью аватара'


try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email_display', 'first_name', 'last_name', 'display_avatar')
    search_fields = ('user__username', 'user__email', 'first_name', 'last_name')
    readonly_fields = ('preview_avatar',)

    def email_display(self, obj):
        return obj.user.email
    email_display.short_description = 'Email'

    def display_avatar(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="40" height="40" style="object-fit: cover; border-radius: 50%;" />', obj.avatar)
        return "Нет фото"
    display_avatar.short_description = 'Аватар'

    def preview_avatar(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="150" style="border-radius: 8px;" />', obj.avatar)
        return "Ссылка на аватар отсутствует"
    preview_avatar.short_description = 'Превью аватара'

