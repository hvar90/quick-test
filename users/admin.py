from django.contrib import admin
from .models import Profile,User

class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('updated_at',) 


#admin.site.register(ProfileAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(User)
