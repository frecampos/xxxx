from django.contrib import admin
from .models import SliderIndex,MisionyVision,Insumos

# Register your models here.
class SliderIndexAdmin(admin.ModelAdmin):
    list_display=['ident','imagen']
    search_fields = ['ident']
    list_per_page = 3

class InsumosAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','descripcion','stock']
    search_fields = ['nombre','descripcion']
    list_per_page = 3

admin.site.register(SliderIndex, SliderIndexAdmin)
admin.site.register(MisionyVision)
admin.site.register(Insumos, InsumosAdmin)
