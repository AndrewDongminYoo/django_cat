from django.contrib import admin
from catfood.models import Formula, Brand
# Register your models here.


class FormulaAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'url', )
    list_filter = ('brand',)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('en_name', 'ko_name', 'site', )


admin.site.register(Formula, FormulaAdmin)
admin.site.register(Brand, BrandAdmin)
