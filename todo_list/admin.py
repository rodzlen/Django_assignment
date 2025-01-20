from django.contrib import admin
from todo_list.models import Todo

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'is_complete','start_date', 'end_date','description')
    list_filter = ('title', 'is_complete')
    list_display_links = ('title','description','start_date','end_date','is_complete')