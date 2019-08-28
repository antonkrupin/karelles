from django.contrib import admin

from .models import Contacts, il_1, vl_1, il_1_citizen,price_300,price_301,price_citizen,contact

class contactAdmin(admin.ModelAdmin):
    list_display = ('name','phone','email','dztype')

admin.site.register(Contacts)
admin.site.register(il_1)
admin.site.register(vl_1)
admin.site.register(il_1_citizen)
admin.site.register(price_300)
admin.site.register(price_301)
admin.site.register(price_citizen)
admin.site.register(contact, contactAdmin)
