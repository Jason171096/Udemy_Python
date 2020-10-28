from django.contrib import admin
from .models import Page

# Register your models here.

def PageAdmin():
    readonly_fields = ('create_at', 'update_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'create_at')

admin.site.register(Page, PageAdmin())

title = "Proyecto"
subtitle = "Panel de gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_header = subtitle