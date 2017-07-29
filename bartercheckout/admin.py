from django.contrib import admin

# Register your models here.
from .models import BarterEvent
from .models import BarterAccount

admin.site.register(BarterAccount)
admin.site.register(BarterEvent)