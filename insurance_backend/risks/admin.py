from django.contrib import admin

# Register your models here.
from .models import Risk, RiskInput
admin.site.register(Risk)
admin.site.register(RiskInput)
