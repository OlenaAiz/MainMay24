from django.contrib import admin
from .models import (BookATour, GetInTouch)


@admin.register(BookATour)
class BookATourAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'date_created', 'date_updated', 'is_confirmed')
    list_filter = ('date_created', 'date_updated', 'is_confirmed', 'date', 'name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
    list_editable = ('is_confirmed', 'date', 'phone')


@admin.register(GetInTouch)
class GetInTouchAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'date_created', 'date_updated', 'is_confirmed')
    list_filter = ('date_created', 'date_updated', 'is_confirmed', 'name', 'email', 'phone')
    search_fields = ('email', 'phone', 'message', 'date_created', 'date_updated', 'is_confirmed')
    list_editable = ('is_confirmed', 'email', 'phone', 'message')
