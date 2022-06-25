from django.db import models
from core.models import BaseModel

# Create your models here.
class Test(BaseModel):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SampleType(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
