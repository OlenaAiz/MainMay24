from django.contrib import admin
from .models import (CreateYourTourStyle, DiscoverNewHorizon, OurServices, HotTours, OurStaff, BookTourNow, Gallery,
                     Contacts, Swiper, HeaderFooter)
from django.utils.safestring import mark_safe
# admin.site.register(CreateYourTourStyle)
# admin.site.register(BookTourNow)
# admin.site.register(OurServices)
# admin.site.register(HotTours)
# admin.site.register(OurStaff)
# admin.site.register(Gallery)
# admin.site.register(Contacts)
admin.site.register(Swiper)
admin.site.register(HeaderFooter)


@admin.register(CreateYourTourStyle)
class CreateYourTourStyleAdmin(admin.ModelAdmin):
    list_display = ('name', 'buttonname', 'is_visible', 'sort')
    list_filter = ('is_visible', 'sort', 'name')
    search_fields = ('name', 'sort')
    list_editable = ('is_visible', 'sort', 'buttonname')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height =50>")
    photo_src_tag.short_description = 'style of tour photo'


@admin.register(DiscoverNewHorizon)
class DiscoverNewHorizonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'buttonname')
    list_editable = ('name', 'description', 'buttonname')
    list_filter = ('buttonname',)
    search_fields = ('name',)


@admin.register(OurServices)
class OurServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'icon')
    list_editable = ('name', 'description', 'icon')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(HotTours)
class HotToursAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'reviewstar', 'reviews', 'tourstyle', 'date',
                    'is_visible')
    list_editable = ('name', 'description', 'price', 'reviewstar', 'reviews', 'tourstyle',
                     'is_visible')
    list_filter = ('name', 'tourstyle', 'date', 'is_visible', 'reviewstar', 'reviews', 'price')
    search_fields = ('name', 'tourstyle', 'date', 'price', 'reviewstar', 'reviews')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height =50>")

    photo_src_tag.short_description = 'tour main photo'


@admin.register(OurStaff)
class OurStaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'photo_src_tag')
    list_editable = ('name', 'position')
    list_filter = ('position',)
    search_fields = ('name', 'position', 'phone_number')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height =50>")

    photo_src_tag.short_description = 'staff person photo'


@admin.register(BookTourNow)
class BookTourNowAdmin(admin.ModelAdmin):
    list_display = ('id', 'description1', 'description', 'buttonname', 'is_confirmed')
    list_editable = ('description1', 'description', 'buttonname', 'is_confirmed')
    list_filter = ('is_confirmed', )
    search_fields = ('description1', 'description', 'buttonname')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height =50>")

    photo_src_tag.short_description = 'style of tour photo'


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name', )
    list_filter = ('name',)
    search_fields = ('name', 'id')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height =50>")

    photo_src_tag.short_description = 'gallery photo'


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone_number', 'facebook_link', 'instagram_link', 'twitter_link')
    list_editable = ('email', 'phone_number', 'facebook_link', 'instagram_link', 'twitter_link')