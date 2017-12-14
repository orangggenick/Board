from django.contrib import admin

from Board.models import Profile, Advertisement, City, Category, Shop, Feedback


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('header','public_date','views','moderated')


admin.site.register(Profile)
admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Feedback)
