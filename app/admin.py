from django.contrib import admin
from app.models import Outlet, Location, UserProfile, Category, Suggestions, Review


class OutletAdmin(admin.ModelAdmin):
    list_display = ('full_name','cat','phone_no_primary',)
    list_filter = ('cat','location')
class CatAdmin(admin.ModelAdmin):
    list_display = ('name','is_active','display_order',)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('outlet','rating',)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('name','city',)
admin.site.register(Outlet,OutletAdmin)
admin.site.register(Location)
admin.site.register(Category,CatAdmin)
admin.site.register(UserProfile)
admin.site.register(Suggestions,SuggestionAdmin)
admin.site.register(Review,ReviewAdmin)