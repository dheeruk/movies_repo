from django.contrib import admin
from .models import AddMoviesModel
# Register your models here.
class AddAdmin(admin.ModelAdmin):
    list_display=['movieName','actorName','actressName','releaseDate','rating']

admin.site.register(AddMoviesModel,AddAdmin)
