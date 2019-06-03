from django.contrib import admin

# Register your models here.
from .models import RiskType, RiskField, FieldOption
admin.site.register(RiskType)
admin.site.register(RiskField)
admin.site.register(FieldOption)
