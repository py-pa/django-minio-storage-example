from django.db import models
from django.db.models import Model


def myfilepath(instance, filename):
    return f"myfiles/{filename}"


class MyFile(Model):
    some_file = models.FileField(upload_to=myfilepath)
