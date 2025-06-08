from django.contrib import admin
from .models import Restaurant,Menu_item,Place

class ReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


#admin.site.register(ReadOnlyAdmin)
admin.site.register(Restaurant,ReadOnlyAdmin)
admin.site.register(Place)
admin.site.register(Menu_item)

