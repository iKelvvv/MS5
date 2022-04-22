from django.contrib import admin
from .models import Post


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug', 'author', 'created_on', 'status')

    search_fields = ('title', 'slug', 'author', 'status',)


admin.site.register(Post, BlogAdmin)
