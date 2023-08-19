from django.contrib import admin

from .models import Phone

class PhoneAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


admin.site.register(Phone, PhoneAdmin)
