from helpers.models import BaseModel
from django.db import models


class TestModel(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)

    @classmethod
    def get_all(cls):
        # print('i am ok')
        # print('again i m ok')
        # print('no again')
        return cls.objects.all()