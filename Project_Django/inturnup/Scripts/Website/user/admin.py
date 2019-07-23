from django.contrib import admin
from .models import Uniuser


class userAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(Uniuser, userAdmin)
