from django.contrib import admin
from foto.models import foto

# Register your models here.
class fotoAdmin(admin.ModelAdmin):
	list_display=['name']

admin.site.register(foto)