from django.contrib import admin
from .models import Order,Delivery,Order_item

class ReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


#admin.site.register(ReadOnlyAdmin)
admin.site.register(Order,ReadOnlyAdmin)
admin.site.register(Order_item)
admin.site.register(Delivery)

