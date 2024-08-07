from django.contrib import admin
from todo_deploy.models import *


# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'done')
    list_filter = ('title', 'done')
    search_fields = ('title',)


admin.site.register(Post)
