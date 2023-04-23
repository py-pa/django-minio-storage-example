from django.contrib import admin
from example.app.models import MyFile


@admin.register(MyFile)
class MyFileAdmin(admin.ModelAdmin):
    pass
