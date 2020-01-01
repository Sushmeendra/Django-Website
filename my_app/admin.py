from django.contrib import admin
from .models import User , Portfolio , Investment
# Register your models here.
admin.site.register(User)
admin.site.register(Portfolio)
admin.site.register(Investment)