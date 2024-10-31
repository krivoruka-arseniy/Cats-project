from django.contrib import admin
from .models import Cats, Users, Messages

admin.site.register(Cats)
admin.site.register(Users)
admin.site.register(Messages)