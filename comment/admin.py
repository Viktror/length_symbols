from django.contrib import admin
from .models import Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'text',)
    list_filter = ("name",)
    search_fields = ('name', 'text')
    #prepopulated_fields = {'slug': ('title',)}


admin.site.register(Comment)
