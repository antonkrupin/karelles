from django.contrib import admin

from .models import Contacts,price_300,price_301,price_citizen,Contact,Photos

class contactAdmin(admin.ModelAdmin):
    list_display = ('name','phone','email','dztype','contact_date')

admin.site.register(Contacts)
admin.site.register(price_300)
admin.site.register(price_301)
admin.site.register(price_citizen)
admin.site.register(Contact, contactAdmin)
admin.site.register(Photos)
