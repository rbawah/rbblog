from django.contrib import admin
from blog.models import Post, Topic, Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'serial_num', 'summary', 'text', 'ogtype', )
    prepopulated_fields = {'slug': ('title',)}

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Category, CategoryAdmin)