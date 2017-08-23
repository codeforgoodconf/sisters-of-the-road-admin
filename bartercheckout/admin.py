from django.contrib import admin

# Register your models here.
from .models import BarterEvent
from .models import BarterAccount


class BarterEventAdmin(admin.ModelAdmin):
	"""
	This is where you modify the view of a BarterEvent in the admin page.
	"""
	
class BarterAccountAdmin(admin.ModelAdmin):
	"""
	This is where you modify the view of a BarterAccount in the admin page.
	"""
admin.site.site_header = 'Sisters of the Road Cafe Admin'
admin.site.index_title = 'Sisters of the Road Checkout Administration'
admin.site.register(BarterAccount)
admin.site.register(BarterEvent)