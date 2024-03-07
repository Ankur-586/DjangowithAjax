from django.contrib import admin
from ajax_form.models import contact_us

class contactAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email_address','website_name','customer_message']
admin.site.register(contact_us,contactAdmin)
