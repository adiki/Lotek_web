from django.contrib import admin

# Register your models here.


from .models import User


class UserAdmin(admin.ModelAdmin):
    fields = ['money', 'randoms']
    list_display = ['money', 'randoms']

admin.site.register(User, UserAdmin)