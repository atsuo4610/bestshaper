from django.contrib import admin

from .models import User, Brassiere


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Brassiere)
class Brassiere(admin.ModelAdmin):
    pass