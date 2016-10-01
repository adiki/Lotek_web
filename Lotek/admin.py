from django.contrib import admin

# Register your models here.


from .models import Result


class ResultAdmin(admin.ModelAdmin):
    fields = ['date', 'number']
    list_display = ['date', 'number']

admin.site.register(Result, ResultAdmin)