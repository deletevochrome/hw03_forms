from django.contrib import admin
# Register your models here.
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    list_editable = ('group',)
    # группы в конце для связи
    search_fields = ('text',)
    list_filter = ('pub_date',)   # фильтрация по дате
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')   # поиск по тексту
    search_fields = ('title',)
    empty_value_display = '-пусто-'


# Регистрация классов
admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
