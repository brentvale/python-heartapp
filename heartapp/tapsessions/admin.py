from django.contrib import admin

# Register your models here.
from .models import Sequence
from .models import HeartBeat

admin.site.register(Sequence)
admin.site.register(HeartBeat)
